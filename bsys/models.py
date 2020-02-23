from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
# from django.contrib.auth.models import User
from django.db import transaction

# Create your models here.

# class CustomUser(AbstractUser):
#     pass

# class Role(models.Model):
#     ROLE_CHOICES = (
#         (1, 'Driver'),
#         (2, 'Admin'),
#     )
#     # id = models.IntegerField(primary_key=True)
#     name = models.CharField(choices=ROLE_CHOICES,max_length=12)
#     def __str__(self):
#         return self.get_id_display()

class User(AbstractUser):
    # roles = models.ForeignKey(
    #     'Role',
    #     on_delete=models.CASCADE,
    #     # null= True
    # )
    is_admin = models.BooleanField("admin status",default=False)
    is_driver = models.BooleanField("driver status",default=False)
    salary = models.FloatField("salary",default=2000)


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __init__(self, *args, **kwargs):
        # self._meta.   get_field('is_admin').default = True
        super(Manager, self).__init__(*args, **kwargs)


class Bus(models.Model):
    """docstring for ."""
    licenceCode = models.CharField(max_length=20,null=True)
    status = models.BooleanField("status",default=False)
    lastCheckUp = models.DateField(null=True)
    def __str__(self):
        return self.licenceCode

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bus = models.OneToOneField(Bus ,null=True,on_delete=models.SET_NULL)
    licenceNum = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.first_name
    def __init__(self, *args, **kwargs):
        # self._meta.get_field('is_driver').default = True
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
