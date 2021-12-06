from django.db import models


# Create your models here.
class Categories(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    category_name = models.CharField(max_length=50)
    parent_category = models.DecimalField(max_length= 4,decimal_places=2)

 def __str__(self):
        return self.category_name


class Books(models.Model):
    category_id = models.ForeignKey(id(Categories),on_delete=models.CASCADE)
    Book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    publish_year = models.CharField()


 def __book__(self):
        return self.Book_name
