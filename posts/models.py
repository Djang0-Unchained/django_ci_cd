from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(null=True, blank=True, max_length=124)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
