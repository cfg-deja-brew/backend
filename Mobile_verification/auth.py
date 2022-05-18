import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app
from werkzeug.security import check_password_hash, generate_password_hash

from db_connection import get_db_connection

from twilio.rest import Client
