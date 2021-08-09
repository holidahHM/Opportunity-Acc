from django.db import models
from accounts.models import Account

DISCOVERY = 'D'
PROPOSAL_SHARED = 'P'
NEGOTIATIONS = 'N'

CHOICES = (
    (DISCOVERY, 'Discovery'),
    (PROPOSAL_SHARED, 'Proposal Shared'),
    (NEGOTIATIONS, 'Negotiations'),
)


class Opportunity(models.Model):
    class Meta:
        verbose_name_plural = "Opportunities"

    title = models.CharField(null=False, max_length=500)
    amount = models.IntegerField(null=False)
    stage = models.CharField(choices=CHOICES, max_length=50)
    associated_account = models.ForeignKey(Account, related_name='account', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
