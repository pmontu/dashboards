from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='static/images/')

    def __str__(self):
    	return "id {} uploaded by {}".format(self.id, self.user)
