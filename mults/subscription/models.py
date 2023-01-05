from django.db import models


# Create your models here.
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
