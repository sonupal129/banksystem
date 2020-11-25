
# Phone Number Library
from phonenumber_field.modelfields import PhoneNumberField

# Django Modules
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import path
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.core.validators import MinValueValidator
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

# Python Lib
import random, hashlib
from decimal import Decimal
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError, PermissionDenied

# Pandas
import pandas as pd

# Djnago Post Office
from post_office import mail as postoffice_mail

# Django Rest Framework
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


# Functions Below

def generateRandomNumbers(start_num, end_num):
    return random.randint(start_num, end_num)
