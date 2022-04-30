from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Order(models.Model):
    name = models.TextField(blank=True)
    price = models.DecimalField(blank=True, decimal_places=5, max_digits=9999)

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='user_address',
                             on_delete=models.CASCADE)
    latitude = models.DecimalField(blank=True, decimal_places=5, max_digits=9999)
    longitude = models.DecimalField(blank=True,decimal_places=5, max_digits=9999)


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='user_Item',
                             on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(blank=True,decimal_places=5, max_digits=9999)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)

    real_name = models.TextField(null=True)
    phone = models.CharField(null=True, max_length=255)
    CUSTOMER = '1'
    DRIVER = '2'
    SERVICE_PROVIDER = '3'
    types = (
    (CUSTOMER, 'CUSTOMER'),
    (DRIVER, 'DRIVER'),
    (SERVICE_PROVIDER, 'SERVICE_PROVIDER'),
)
    Type = models.CharField(
        max_length=2,
        choices=types,
        default=CUSTOMER
    )
    def __str__(self):
        return f'Profile for user {self.user.username}'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

