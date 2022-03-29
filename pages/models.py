from django.db import models
from django.contrib.auth.models import User

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Assets = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    Staked = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    Profits = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.user.username} Balance'
    
