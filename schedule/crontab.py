from datetime import datetime

import pytz

from config import settings
from schedule.models import Newsletter


def do():
    from schedule.task_for_mailing import (
        create_daily_task,
        create_weekly_task,
        create_monthly_task,
    )

    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # Код, который будет выполнен при запуске
    create_daily_task()
    create_weekly_task()
    create_monthly_task()
    newsletter = Newsletter.objects.all()
    for post in newsletter:
        print(f"POST: {current_datetime}, {post.pk}, {post.status_of_newsletter}")