from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,  # for all many-to-one relationships we must to specify on_delete!
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    # reverse helps to reference an object by its URL template name
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
