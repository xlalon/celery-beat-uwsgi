# -*- coding: utf8 -*-

from flask import Flask


def create_app(celery_init_app_func=None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://redis:6379",
            result_backend="redis://redis:6379",
            task_ignore_result=False,
            timezone="Asia/Shanghai",
        ),
    )
    app.config.from_prefixed_env()
    if celery_init_app_func:
        celery_init_app_func(app)
    return app
