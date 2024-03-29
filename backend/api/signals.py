from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount



@receiver(post_save, sender=SocialAccount)
def add_extra_data_to_the_user(sender, instance, created, *args, **kwargs):
    # instance.user.photo = instance.extra_data['picture']
    instance.user.save()