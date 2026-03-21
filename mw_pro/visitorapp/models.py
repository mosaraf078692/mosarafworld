from django.db import models

class Visitor(models.Model):

    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, null=True, blank=True)

    browser = models.CharField(max_length=100, null=True, blank=True)
    device = models.CharField(max_length=100, null=True, blank=True)

    path = models.CharField(max_length=500)

    is_unique = models.BooleanField(default=False)

    visit_date = models.DateField(auto_now_add=True)
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.path}"