from application import app
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session


@app('/index')
def index():
    return "<h1>Hello Earth!<h1>"