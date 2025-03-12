# -*- coding: utf8 -*-

from flask import Flask
from celery import Celery, Task


def celery_init_app(flask_app: Flask) -> Celery:

    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    flask_app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://redis:6379",
            result_backend="redis://redis:6379",
            task_ignore_result=False,
            timezone="Asia/Shanghai",
        ),
    )

    app = Celery(flask_app.name, task_cls=FlaskTask, include=["core.tasks"])
    app.config_from_object(flask_app.config["CELERY"])
    app.set_default()
    app.conf.beat_schedule = {
        'print-timestamp-10times-every-seconds': {
            'task': 'core.tasks.print_timestamp',
            'schedule': 0.1,
        },
    }
    flask_app.extensions["celery"] = app
    return app
