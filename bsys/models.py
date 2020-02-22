from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
# from django.contrib.auth.models import User
from django.db import transaction

# Create your models here.

# class CustomUser(AbstractUser):
#     pass

class Role(models.Model):
    ROLE_CHOICES = (
        (1, 'Driver'),
        (2, 'Admin'),
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    def __str__(self):
        return self.get_id_display()

class User(AbstractUser):
    roles = models.ForeignKey(
        'Role',
        on_delete=models.CASCADE,
        default='Driver'
    )


class PrivilegedUser(User):
    # fName = models.CharField(max_length=30)
    # lName = models.CharField(max_length=30)
    # email = models.EmailField(_('email address'), unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    # def __str__(self):
    #     return self.email
    pass

# class Driver(CustomUser):
#     """docstring for ."""
#     # licence_numeber = models.CharField(max_length=30)
#     # def __init__(self, arg):
#     #     super(, self).__init__()
#     #     self.arg = arg
#     pass

class Bus(models.Model):
    """docstring for ."""

    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg
    pass

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bus = models.OneToOneField(Bus ,null=True,on_delete=models.SET_NULL)
    def __init__(self, *args, **kwargs):
        self._meta.get_field('roles').default = 'Driver'
        super(Driver, self).__init__(*args, **kwargs)

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
