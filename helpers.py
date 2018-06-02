from flask import flash as _flash


class endpoints():
    HOME = '/'
    REDIRECT = '/redirect'


class flash():

    @staticmethod
    def info(message):
        return _flash(message, category='info')

    @staticmethod
    def error(message):
        return _flash(message, category='error')

