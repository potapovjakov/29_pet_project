"""Модели приложения users."""
from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


MALE = 'male'
FEMALE = 'female'

GENDER_CHOICES = ((MALE, 'Мужской'), (FEMALE, 'Женский'))


class Profile(models.Model):
    """Класс профиля User, расширяет модель User. Доступ user.profile."""

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=False)
    photo = models.ImageField('Аватар', upload_to='users/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создает Profile при создании User."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Сохраняет Profile, при сохранении User."""
    instance.profile.save()
