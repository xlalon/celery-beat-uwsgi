# -*- coding: utf8 -*-

import time
from celery import shared_task


@shared_task(ignore_result=False)
def print_timestamp() -> int:
    return int(time.time() * 10)
