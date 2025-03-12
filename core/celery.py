# -*- coding: utf8 -*-

from flask import Flask
from celery import Celery, Task


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask, include=["core.tasks"])
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    celery_app.conf.beat_schedule = {
        'aoto-increment-every-1-seconds': {
            'task': 'core.tasks.auto_increment',
            'schedule': 0.5,
            'args': ('test_key',),
        },
    }
    app.extensions["celery"] = celery_app
    return celery_app
