from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField("First Name", max_length=255)
    last_name = models.CharField("Last Name", max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    last_log_in = models.DateTimeField("Last Log In", auto_now_add=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name