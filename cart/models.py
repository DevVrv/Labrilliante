from django.db import models

from users.models import CustomUsers

# Create your models here.
class CartModal(models.Model):
    user = models.ForeignKey(CustomUsers, verbose_name="User Cart", db_index=True, on_delete=models.CASCADE)
    user_cart = models.JSONField(verbose_name='User Cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'User Cart'
        verbose_name_plural = 'User Cart'
