from django.db import models
from django.core.validators import MinValueValidator
from main.models import CustomUser
from .constants import (
    CLASS_CHOICES, RACE_CHOICES, ROLE_CHOICES, FACTION_CHOICES
)


class CharacterClass(models.Model):
    """Класс персонажа."""

    name = models.CharField(
        max_length=50,
        choices=CLASS_CHOICES,  # используем константы
        unique=True,
        verbose_name='Класс'
    )
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
    
    def __str__(self):
        return self.get_name_display()


class Race(models.Model):
    """Раса персонажа."""

    name = models.CharField(
        max_length=50,
        choices=RACE_CHOICES,  # используем константы
        unique=True,
        verbose_name='Раса'
    )
    faction = models.CharField(
        max_length=10,
        choices=[
            ('alliance', 'Альянс'),
            ('horde', 'Орда'),
        ],
        verbose_name='Фракция'
    )
    
    class Meta:
        verbose_name = 'Раса'
        verbose_name_plural = 'Расы'
    
    def __str__(self):
        return self.get_name_display()


class Specialization(models.Model):
    """Специализация персонажа."""

    character_class = models.ForeignKey(
        CharacterClass,
        on_delete=models.CASCADE,
        related_name='specializations',
        verbose_name='Класс'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Специализация'
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        verbose_name='Роль'
    )
    
    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'
        unique_together = [('character_class', 'name')]
    
    def __str__(self):
        return f'{self.name} ({self.character_class.get_name_display()})'


class Character(models.Model):
    """Персонаж пользователя."""
    name = models.CharField(
        max_length=16,
        verbose_name='Имя персонажа',
        help_text='2-16 символов'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='characters',
        verbose_name='Владелец',
        null=True,
        blank=True
    )
    character_class = models.ForeignKey(
        'CharacterClass',
        on_delete=models.PROTECT,
        related_name='characters',
        verbose_name='Класс'
    )
    specialization = models.ForeignKey(
        'Specialization',
        on_delete=models.PROTECT,
        related_name='characters',
        verbose_name='Специализация'
    )
    race = models.ForeignKey(
        'Race',
        on_delete=models.PROTECT,
        related_name='characters',
        verbose_name='Раса'
    )
    faction = models.CharField(
        max_length=10,
        choices=FACTION_CHOICES,
        verbose_name='Фракция'
    )
    item_level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name='Уровень предметов'
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name='Основной персонаж'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
        ordering = ['-created_at']
        # Уникальность: один персонаж с таким именем
        unique_together = [('name', 'user')]
    
    def clean(self):
        """Проверяем согласованность данных."""
        from django.core.exceptions import ValidationError
        
        # Проверяем, что специализация принадлежит классу
        if self.specialization.character_class != self.character_class:
            raise ValidationError(
                f'Специализация {self.specialization} не принадлежит классу {self.character_class}'
            )
        
        # Проверяем, что раса соответствует фракции
        if self.race.faction != self.faction:
            raise ValidationError(
                f'Раса {self.race} принадлежит фракции {self.race.faction}, '
                f'а выбрана фракция {self.faction}'
            )
    
    def __str__(self):
        return f'{self.name} ({self.character_class.get_name_display()})'
