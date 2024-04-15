from django.db import models

class Input(models.Model):
    value = models.FloatField(help_text="Enter a value to process with the algorithm.")
