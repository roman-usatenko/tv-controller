import json
import os
from flask import Flask, render_template, redirect, request
import tv
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
BUTTONS = {}


@app.route('/')
def index():
    return render_template('index.html',
                           tv_state=tv.get_state(),
                           buttons=BUTTONS.values())


@app.route('/off')
def hello_world():
    tv.off()
    return redirect("/", code=302)


@app.route('/button/<btn>')
def button(btn):
    b = BUTTONS.get(btn)
    if b:
        tv.do_script(b['script'])
    return redirect("/", code=302)


@app.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'


def load_buttons():
    dir, file = os.path.split(os.path.abspath(__file__))
    with open(os.path.join(dir, 'buttons.json')) as json_data:
        btns = json.load(json_data)
    for btn in btns:
        BUTTONS[btn["id"]] = btn


if __name__ == "__main__":
    load_buttons()
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        tv.cleanup()
