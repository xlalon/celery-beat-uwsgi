# -*- coding: utf8 -*-

from celery import shared_task

from .redis import redis


@shared_task(ignore_result=False)
def auto_increment(key: str) -> int:
    result = int(redis.get(key) or 0)
    redis.set(key, result + 1)
    return result
