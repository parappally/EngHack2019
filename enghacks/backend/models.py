from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, blank=False, unique=True)
    email = models.EmailField()
    city = models.CharField(max_length=30)

class UserHealthInformation(models.Model):
    sex_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='health_information',
    )
    sex = models.CharField(
        max_length=6,
        choices=sex_choices,
        null=True,
    )
    date_of_birth = models.DateField(
        auto_now = False,
        null=True,
        blank=True
    )
    allergies = ArrayField(
        models.CharField(max_length=30, blank=True),
        null=True,
        size=20
    )

class DirectionThread(models.Model):

    current_step_options = [
        ('USER_LOCATION', 'USER_LOCATION'),
        ('DESTINATION', 'DESTINATION'),
        ('DEST_CHOICES', 'DEST_CHOICES'),
        ('TRANS', 'TRANS')
        ('ARRIVED', 'ARRIVED'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    current_step = models.CharField(
        max_length=13,
        choices=current_step_options,
        default=current_step_options[0][0]
    )
    date_time = models.DateTimeField(
        auto_now=True,
    )
    start_location = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    end_location = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    completed_at = models.DateTimeField(
        null=True,
        auto_now=False,
    )

    def increment_step(self):
        current_step = self.current_step
        current_step_index = self.current_step_options.index(current_step)

        self.update(
            current_step=self.current_step_options[current_step_index + 1]
        )

    def store_data(self):
        if self.current_step == 'USER_LOCATION':
            self.start_location = request_body
        elif self.current_step == 'DESTINATION':
            self.end_location == request_body
        



class Place(models.Model):
    direction_thread = models.ForeignKey(
        DirectionThread,
        on_delete=models.CASCADE,
        related_name='places_list'
    )
    name = models.CharField(
        max_length=50,
        blank=False,
    )
    distance = models.DecimalField(
        decimal_places=1,
        blank=False,
        max_digits=4,
    )
    address = models.CharField(
        max_length=100,
        blank=False,
    )
    estimated_time = models.DurationField(
        blank=False,
    )
