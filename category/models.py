from django.db import models

# Create your models here.

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class CountryCategory(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Category)
def category_rpe_save(sender, instance, *args, **kwargs):
    # print(sender, '!!!!!!!!!!!!!!')
    # print(instance, '--------------')
    if not instance.slug:
        instance.slug = slugify(instance.name)
