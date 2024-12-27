from django.db import models
from accounts.models import CustomUser


# Create your models here.


class Order(models.Model):
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    grain_type = models.CharField(max_length=100, default='wheat')
    quantity = models.PositiveIntegerField(default=1)
    APPROVED = "AP"
    PENDING = "PE"
    STATUS = (
        (APPROVED, "Approved"),
        (PENDING, "Pending")
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
