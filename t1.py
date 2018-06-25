# -*- coding: utf-8 -*-
from django.db import models
from jsonfield import JSONField

class Test(models.Model):
    """
    Represents a Test
    description = models.TextField('Test')

