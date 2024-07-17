from datetime import datetime
from random import shuffle
from smtplib import SMTPException

import pytz
from django.conf import settings
from django.core.cache import cache

from django.core.mail import send_mail
from django.shortcuts import redirect

from blog.models import Blog
from config.settings import EMAIL_HOST_USER
from schedule.models import Log, DONE, Newsletter, IN_WORK


def send_mailing(mailing):
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    current_time_formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S%z")
    time_obj = datetime.strptime(current_time_formatted, "%Y-%m-%d %H:%M:%S%z")

    # Проверяем, должна ли рассылка выполняться в данный момент времени
    if mailing.start_time <= time_obj <= mailing.end_time:
        try:
            for client in mailing.clients.all():
                message = mailing.message
                result = send_mail(
                    subject=message.subject,
                    message=message.text,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[client.contact_email],
                    fail_silently=False,
                )
                # Создаем объект Log для записи в журнал
                log = Log.objects.create(
                    time_attempt=current_datetime,
                    status_of_last_attempt=bool(result),
                    server_response="OK" if result else "Error",
                    mailing_list=mailing,
                    client=client,
                    company=client.company,
                )
                log.save()

        except SMTPException as error:
            # Если произошла ошибка при отправке, создаем объект Log с соответствующими данными
            log = Log.objects.create(
                time_attempt=current_datetime,
                status_of_last_attempt=False,
                server_response=str(error),
                mailing_list=mailing,
            )
            log.save()
        if mailing.end_time <= time_obj:
            mailing.status_of_newsletter = DONE
        elif mailing.end_time >= time_obj:
            mailing.status_of_newsletter = IN_WORK

    mailing.save()


def toggle_activity(request, pk):
    mailing = Newsletter.objects.get(pk=pk)
    if mailing.is_active:
        mailing.is_active = False
    else:
        mailing.is_active = True

    mailing.save()
    return redirect("schedule:newsletter_list")


def get_cached_blog(request):
    blogs_list = cache.get("cached_blogs_list")
    if not blogs_list:
        blog_pks = list(Blog.objects.values_list("pk", flat=True))
        shuffle(blog_pks)
        selected_blog_pks = blog_pks[:3]
        blogs_list = Blog.objects.filter(pk__in=selected_blog_pks)
        cache.set("cached_blogs_list", blogs_list, 60 * 5)
    return blogs_list