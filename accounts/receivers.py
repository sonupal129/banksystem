from .imports import *
from .models import UserProfile

# CODE Below

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


def sendTransactionEmail(sender, instance, created, **kwargs):
    # class tasks
    pass


