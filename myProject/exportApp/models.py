from django.db import models

class User(models.Model):
    userId=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age =models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):
        return self.first_name

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateOfJoining=models.DateField()
    typeOfMembership=models.CharField(max_length=20)
    def __str__(self):
        return self.typeOfMembership
