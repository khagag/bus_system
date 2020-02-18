from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

class PrivilegedUser(CustomUser):
    # fName = models.CharField(max_length=30)
    # lName = models.CharField(max_length=30)
    # email = models.EmailField(_('email address'), unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    # def __str__(self):
    #     return self.email
    pass

class Driver(models.Model):
    """docstring for ."""
    # licence_numeber = models.CharField(max_length=30)
    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg
    pass

class Bus(models.Model):
    """docstring for ."""

    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg
    pass

class RoadLines(models.Model):
    """docstring for ."""

    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg
    pass

class StopStations(models.Model):
    pass

class Areas(models.Model):
    """docstring for areas."""

    # def __init__(self, arg):
    #     super(areas, self).__init__()
    #     self.arg = arg
    pass

class Config(models.Model):
    """docstring for config."""
    #
    # def __init__(self, arg):
    #     super(config, self).__init__()
    #     self.arg = arg
    pass
