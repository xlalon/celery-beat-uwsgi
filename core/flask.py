# -*- coding: utf8 -*-

from flask import Flask


def create_app(celery_init_app=None) -> Flask:
    app = Flask(__name__)
    app.config.from_prefixed_env()
    if celery_init_app:
        celery_init_app(app)
    return app
