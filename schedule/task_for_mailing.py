from datetime import timedelta

from schedule.models import Newsletter, DAILY, CREATE, WEEKLY, MONTHLY, IN_WORK
from schedule.services import send_mailing


def create_task_for_frequency(frequency, interval):
    mailings = Newsletter.objects.prefetch_related("clients", "message").filter(
        frequency=frequency, status_of_newsletter__in=[CREATE, IN_WORK], is_active=True
    )
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)
            mailing.start_time += timedelta(days=interval)
            mailing.save()


def create_daily_task():
    create_task_for_frequency(DAILY, 1)


def create_weekly_task():
    create_task_for_frequency(WEEKLY, 7)


def create_monthly_task():
    create_task_for_frequency(MONTHLY, 30)