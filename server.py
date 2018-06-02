from flask import Flask, redirect, request, render_template
from uuid import uuid1
from validators import url as validate_url

from helpers import flash, endpoints


app = Flask(__name__)
app.secret_key = str(uuid1())



@app.route(endpoints.HOME)
def home():
    return render_template('index.html')


@app.route(endpoints.REDIRECT)
def do_redirect():
    url = request.args.get('url', '')
    if not validate_url(url):
        flash.error('Invalid url: "{}"'.format(url))
        return redirect(endpoints.HOME)
    return redirect(url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
