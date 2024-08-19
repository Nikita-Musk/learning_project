from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    last_name = models.CharField(max_length=100, verbose_name='last_name')
    avatar = models.ImageField(upload_to='students/', verbose_name='avatar', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='learning')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ('last_name',)
