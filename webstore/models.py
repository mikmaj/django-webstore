from django.db import models
from django.contrib.auth.models import User


class StoreItem(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description_short = models.CharField(max_length=150)
    description = models.TextField()
    # Use a date based on when the record gets added
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # on_delete specifies what happens to the item if the User who added it gets deleted. SET_NULL = set the author to null
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(default='default.jpg', upload_to='item_pics')

    def __str__(self):
        return self.name

