from django.db import models

class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    description = models.TextField(max_length=500)
    star_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
