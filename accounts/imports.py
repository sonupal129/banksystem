from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random, hashlib
from django.urls import path
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.core.validators import MinValueValidator
from decimal import Decimal
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
import pandas as pd
from django.conf import settings
from post_office import mail as postoffice_mail


# Functions Below

def generateRandomNumbers(start_num, end_num):
    return random.randint(start_num, end_num)
