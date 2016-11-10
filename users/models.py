from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractBaseUser):
    username = models.CharField(
    	"Name",
    	max_length=50,
		error_messages = {
			'required': 'Username is required.'
		}
    )
    birthday = models.DateField(
    	"Birthday",
    	error_messages = {
			'required': 'Birthday is required.'
		}
    )
    random_number = models.IntegerField(
    	"Random Number",
        validators = [MinValueValidator(1), MaxValueValidator(100)],
    	error_messages = {
			'required': 'Random number is required.',
            'max_value': 'The value should be less than 100.',
            'min_value': 'The value should be greater than 0.'
		}
	)
