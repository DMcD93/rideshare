from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Users_Reg(models.Model):
    """
    creating database for all users i.e. driver passenger etc
    email = '2226353k@student.gla.ac.uk' required
    user_type = 1 or 2 (1 = driver, 2 = passenger)
    """
 #   first_name = models.CharField(max_length=30)
  #  last_name = models.CharField(max_length=30)
   # email = models.EmailField(unique=True)

    user = models.OneToOneField(User)

    phone = models.BigIntegerField()
    age = models.IntegerField(null=True)
    identity_number = models.CharField(max_length=30)
		
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
		
    class Meta:
        db_table = "users"


class Vehicle(models.Model):
    """
    Creating database to store vehicle information
    make = "ford"
    """
    reg_no = models.CharField(max_length=8)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    no_of_seats = models.SmallIntegerField(default=1,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])
    user = models.ForeignKey(User)

    class Meta:
        db_table = "vehicle"


class Journey(models.Model):
    """
    Creating database to store user journey details
    """
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travelling_date = models.DateField(null = True)
    travelling_time = models.TimeField(null = True)
    is_return = models.BooleanField(default=False)
	#cost = models.DecimalField(max_digits=2, decimal_places=2), null=True)
    #user = models.ManyToManyField(User)
	#vehicle = user = models.ForeignKey(Vehicle)

    class Meta:
        db_table = "journey"


class Review(models.Model):
    """
    Creating database to store reviews from passengers
    """
    description = models.TextField()
    posted_at = models.DateTimeField()
    user = models.ForeignKey(User)

    class Meta:
        db_table = "review"






















