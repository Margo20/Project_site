from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class RepairsModel(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    def get_absolute_url(self):
        return reverse('rem:ourwork_list_by_repair',
                        args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Вид ремонта'
        verbose_name_plural = 'Виды ремонта'


class OurworkModel(models.Model):
    repair = models.ForeignKey(RepairsModel, related_name='ourworkm', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    image = models.ImageField(upload_to='rem/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse('rem:ourwork_detail',
                        args=[self.id, self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Пример выполненного нами ремонта'
        verbose_name_plural = 'Примеры выполненного нами ремонта'


class contactsModel(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Введите Ваше имя')
    phone = models.CharField(max_length=30, db_index=True, unique=True, verbose_name='Введите Ваш номер телефона')
    email = models.CharField(max_length=30, db_index=True, unique=True, verbose_name='Введите Ваш Email')
    description = models.TextField(max_length=1500, null=True, blank=True, verbose_name='Опишите объект:')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
        ordering = ['-published']


class FooterModel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Ваше имя')
    phone = models.CharField(max_length=15, verbose_name='Ваш телефон')
    email = models.CharField(max_length=30, db_index=True, verbose_name='Введите Ваш Email')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-published']


class OrderCalculationModel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Ваше имя')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    description = models.TextField(max_length=1500, null=True, blank=True, db_index=True, verbose_name='Ремонт')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расчет стоимости косметического ремонта'
        verbose_name_plural = 'Расчеты стоимости косметического ремонта'
        ordering = ['-published']


class KapRemModel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Ваше имя')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    description = models.TextField(max_length=1500, null=True, blank=True, db_index=True, verbose_name='Ремонт')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расчет стоимости капитального ремонта'
        verbose_name_plural = 'Расчеты стоимости капитального ремонта'
        ordering = ['-published']


class EuroRemModel(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Ваше имя')
    phone = models.CharField(max_length=15, verbose_name='Ваш номер телефона')
    description = models.TextField(max_length=1500, null=True, blank=True, db_index=True, verbose_name='Ремонт')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расчет стоимости евроремонта'
        verbose_name_plural = 'Расчеты стоимости евроремонта'
        ordering = ['-published']


class DiscountModel(models.Model):
    phone = models.CharField(max_length=15, verbose_name='Ваш телефон')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Когда и во сколько')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Запрос на скидку'
        verbose_name_plural = 'Запросы на скидку'
        ordering = ['-published']


class DataModelUser(models.Model):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=150)


class ExtendUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')

    class Meta(AbstractUser.Meta):
        pass

# class CustomUser(AbstractUser):
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         ProfileUsers.objects.get_or_create(user=self)