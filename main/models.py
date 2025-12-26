from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import (validate_email, validate_name, validate_nickname,
                         validate_password)


class CustomUser(AbstractUser):
    """Модель кастомного пользователя."""

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_nickname],
        verbose_name='Пользователь',
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        validators=[validate_email],
        verbose_name='Электронная почта',
    )
    first_name = models.CharField(
        max_length=150,
        validators=[validate_name],
        verbose_name='Имя',
    )
    password = models.CharField(
        max_length=150,
        validators=[validate_password],
        verbose_name='Пароль',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
        unique_together = [('username', 'email')]

    def __str__(self) -> str:
        return f'{self.username}: {self.email}'
