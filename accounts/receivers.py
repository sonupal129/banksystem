from .imports import *
from .models import *
from .tasks import sendEmail
# CODE Below

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Transaction)
def sendTransactionEmail(sender, instance, created, **kwargs):
    if created:
        # sendEmail.delay([instance.account.user.user.email], "test_template") # Uncomment this line to start sending email
        return True
    