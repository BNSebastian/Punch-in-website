from django.conf import settings
from django.db import models
import datetime

class jobs(models.Model):
    reason = models.CharField(
        'Motive',
        max_length=255,
        # default='',
        # unique=True,
    )
    description = models.CharField(
        'Description',
        max_length=255,
        null=True,
        # default='',
        # unique=True,
    )
    date = models.DateField(
        'Date:',
        default=datetime.date.today,
    )
    start_date = models.TimeField(
        'Started at:',
        default=datetime.date.today,
    )
    end_date = models.TimeField(
        'Ended at:',
        default=datetime.date.today,
    )
    
    # Foreign key
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
