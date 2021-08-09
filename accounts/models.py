from django.db import models


class Account(models.Model):
    account_name = models.CharField(max_length=50, null=False)
    contact = models.IntegerField(null=False)
    address = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.account_name
