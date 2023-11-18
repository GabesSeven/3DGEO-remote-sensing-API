import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.text import slugify


class CustomUser(AbstractUser):
    """
    Banco de dados de usuário customizado (diferente dos padrões do Django)
    """
    pass
    


