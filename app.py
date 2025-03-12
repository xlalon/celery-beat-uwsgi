# -*- coding: utf8 -*-

from core.celery import celery_init_app
from core.flask import create_app


flask_app = create_app(celery_init_app)
celery_app = flask_app.extensions["celery"]
