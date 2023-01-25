from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory, Post
from django.conf import settings


def send_notifications (Preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text' : Preview,
            'link' : f'{settings.SITE_URL}/news/{pk}',
        }

    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers

    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

# @receiver(post_save, sender=Post)
# def notify_about_new_post(sender, instance, created, **kwargs):
# #     if kwargs['action'] == 'post_add':
# #         categories = instance.postCategory.all()
# #         subscribers = []
# #         for category in categories:
# #             subscribers += category.subscribers.all()
# #
# #         subscribers = [s.email for s in subscribers]
#     if created and instance.__class__.__name__ == 'Post':
#         send_notifications.apply_async((instance.Preview(), instance.pk, instance.title, subscribers),
#                                        countdown=10)
