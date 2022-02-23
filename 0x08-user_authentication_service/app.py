#!/usr/bin/env python3
""" Module called app """


from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def message_welcome():
    """ Return a JSON payload of the welcome message """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """End-point to register a user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login_sessions():
    """ Implement a login function to respond to the POST /sessions route """
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        sessionID = AUTH.create_session(email)
        res = jsonify({
            "email": email,
            "message": "logged in"})
        res.set_cookie('session_id', sessionID)
        return res
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
