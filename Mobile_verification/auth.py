import functools

from flask import (flash, g, redirect, render_template, request, session, url_for
                   )
from flask import current_app as app

from db_connection import get_db_connection

from twilio.rest import Client

# Initialize Twilio client
client = Client()


# currently missing function to check if user is logged in

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db_connection().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


def start_verification(to, channel='sms'):
    if channel not in ('sms', 'call'):
        channel = 'sms'

    service = app.config.get("VERIFICATION_SID")

    verification = client.verify \
        .services(service) \
        .verifications \
        .create(to=to, channel=channel)

    return verification.sid


def check_verification(phone, code):
    service = app.config.get("VERIFICATION_SID")

    try:
        verification_check = client.verify \
            .services(service) \
            .verification_checks \
            .create(to=phone, code=code)

        if verification_check.status == "approved":
            db = get_db_connection()
            db.execute(
                'UPDATE USERS SET MobileConfirmed = TRUE WHERE Mobile = ?',
                (phone,)
            )
            db.commit()
            flash('Your phone number has been verified! Please login to continue.')
            return redirect(url_for('auth.login'))
        else:
            flash('The code you provided is incorrect. Please try again.')
    except Exception as e:
        flash("Error validating code: {}".format(e))

    return redirect(url_for('auth.verify'))


@app.get('/signup', methods=('GET', 'POST'))
def register():
    """Register a new user.
    Validates that the mobile number is not already taken.
    """
    if request.method == 'POST':
        firstname = request.form['FirstName']
        lastname = request.form['LastName']
        phone = request.form['Mobile']
        email = request.form['Email']
        channel = request.form['channel']

        db = get_db_connection()
        error = None

        if not firstname:
            error = 'First name is required.'
        elif not lastname:
            error = 'Last name is required.'
        elif not phone:
            error = 'Mobile number is required'
        elif not email:
            error = 'E-mail address is required'
        elif db.execute(
                'SELECT Id FROM USERS WHERE Mobile = ?', (phone,)
        ).fetchone() is not None:
            error = 'The number {0} is already registered.'.format(phone)

        if error is None:
            session['phone'] = phone
            vsid = start_verification(phone, channel)

            if vsid is not None:
                # the verification was sent to the user and the username is valid
                # redirect to verification check
                db.execute(
                    'INSERT INTO USERS (FirstName, LastName, Email, Mobile) VALUES (?, ?, ?, ?)',
                    (firstname, lastname, email, phone)
                )
                db.commit()
                return redirect(url_for('auth.verify'))

        flash(error)
    return render_template('auth/register.html')


@app.get('/verify', methods=('GET', 'POST'))
def verify():
    """Verify a user on registration with their phone number"""
    if request.method == 'POST':
        phone = session.get('Mobile')
        code = request.form['code']
        return check_verification(phone, code)

    return render_template('auth/verify.html')


@app.get('/login', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == 'POST':
        phone = request.form['Mobile']
        # password = request.form['password']
        db = get_db_connection()
        error = None
        user = db.execute(
            'SELECT * FROM USERS WHERE Mobile = ?', (phone,)
        ).fetchone()

        if phone is None:
            error = 'Incorrect mobile'
        # elif not check_password_hash(user['password'], password):
        #     error = 'Incorrect password.'

        if error is None:
            # store the user id in a new session and return to secret content
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for(''))  # location to be added

        flash(error)

    return render_template('auth/login.html')


@app.get('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('auth.login'))
