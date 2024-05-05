from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=20, unique=True)
    phone_number = PhoneNumberField('Номер телефона', unique=True)
    about = models.TextField('О себе', blank=True)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
    picture = models.ImageField('Фото', upload_to='pictures', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.nickname

class UserChats(models.Model):
    nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_nickname = models.CharField(max_length=20)
    message_value = models.IntegerField(default=0)
    is_pinned = models.BooleanField('Закрепленный чат', default=False)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return f'Чат пользователя {self.nickname} с {self.chat_nickname}'
