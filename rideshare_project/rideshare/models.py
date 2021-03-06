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

    phone = models.BigIntegerField(validators=[MaxValueValidator(99999999999)])
    age = models.IntegerField(null=True, default=18,
        validators=[
            MaxValueValidator(80),
            MinValueValidator(16)
        ])
    identity_number = models.CharField(max_length=8)
		
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
    user = models.ForeignKey(User, primary_key=True)

    class Meta:
        db_table = "vehicle"
		
    def __unicode__(self):
        return self.user.username


class Journey(models.Model):
    """
    Creating database to store user journey details
    """
    journey = models.AutoField(primary_key=True)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travelling_date = models.DateField(null = True)
    travelling_time = models.TimeField(null = True)
    seatsAvailable = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ])
    cost = models.IntegerField(
        validators=[
            MaxValueValidator(50),
            MinValueValidator(0)
        ])
    user = models.ForeignKey(Vehicle, related_name='driver', null=True)

    class Meta:
        db_table = "journey"

    def __str__(self):
        return 'Journey: %s' % + self.pk
		
class Passanger(models.Model):
    front = models.ForeignKey(User, related_name='front', null=True)
    backLeft = models.ForeignKey(User, related_name='backLeft', null=True)
    backRight = models.ForeignKey(User, related_name='backRight', null=True)
    journey = models.ForeignKey(Journey, primary_key=True)

    class Meta:
        db_table = "passanger"
        """ unique_together = (('front', 'backLeft'), ('front', 'backRight'), ('backLeft', 'backRight'), ('front', 'backLeft', 'backRight'))"""
		
    def __str__(self):
        return 'Passangers for Journey: %s' % + self.pk
		
class Review(models.Model):
    """
    Creating database to store reviews from passengers
    """
    description = models.TextField(max_length=150, null=True)
    posted_at = models.DateTimeField()
    posted_by = models.TextField(max_length=30, null=True)
    user = models.ForeignKey(User)

    class Meta:
        db_table = "review"
		
    def __str__(self):
        return 'Review: %s' % + self.pk