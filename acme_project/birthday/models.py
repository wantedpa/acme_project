# birthday/models.py
from django.db import models

from birthday.validators import real_age
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', blank=True, upload_to='birthday_images')
    author = models.ForeignKey(
    User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True,
    related_name='birthdays'
    ) 

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk}) 