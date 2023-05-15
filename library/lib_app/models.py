from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=250, null=False)
    publisher_name =  models.CharField(max_length=250)
    book_type = models.IntegerField()


    def __str__(self):
        return self.book_name
