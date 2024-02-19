from .models import Goods, Tag
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save,sender=Goods)
def handle(sender, **kwargs):
    print(f'Goods {sender.name} is created')

@receiver(post_save,sender=Goods)
def tag_handle(sender, **kwargs):
    print(f'Goods {kwargs["instance"]} is created')
    send_mail(
        'Tag is created',
        f'Tag {kwargs["instance"]} is created',
        'from@yourdjangoapp.com',
        ['to@yourbestuser.com'],
        fail_silently=False,
    )

from django.core.mail import EmailMessage

email = EmailMessage(
    subject = 'That is your subject',
    body = 'That is your massage body',
    from_email = 'from@yourdjangoapp.com',
    to = ['to@yourbestuser.com'],
    bcc = ['bcc@anotherbestuser.com'],
    reply_to = ['whoever@itmaybe.com'],
)

