import settings

from flask import Flask, redirect, request, render_template
from validators import url as validate_url


app = Flask(__name__)
app.secret_key = settings.FLASK_SECRET_KEY


class endpoints():
    HOME = '/'
    REDIRECT = '/redirect'


@app.route(endpoints.HOME)
def home():
    return render_template('index.html')


@app.route(endpoints.REDIRECT)
def do_redirect():
    url = request.args.get('url', '')
    if not validate_url(url):
        return render_template('invalid-url.html', url=url)
    return redirect(url)


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)
