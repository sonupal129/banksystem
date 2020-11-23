from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random


# Functions Below

def generateRandomNumbers(start_num, end_num):
    return random.randint(start_num, end_num)
