from django.contrib.auth.models import User
from galeria.models import Veiculo
from django.db import models

class Favorito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Veiculo, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.username} favorited {self.item}"