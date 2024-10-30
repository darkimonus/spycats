from django.db import models
from cats.models import SpyCat
from django.core.exceptions import ValidationError


class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE, related_name="missions", blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission for {self.cat.name} - {'Complete' if self.is_complete else 'Incomplete'}"

    def delete(self, *args, **kwargs):
        if self.cat is not None:
            raise ValidationError("Mission cannot be deleted as it is assigned to a cat.")
        super().delete(*args, **kwargs)


class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="targets")
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Target {self.name} - {'Complete' if self.is_complete else 'Incomplete'}"
