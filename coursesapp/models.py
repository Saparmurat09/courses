from django.db import models


class Category(models.Model):
    # Model for representing categories of courses
    name = models.CharField(max_length=100, help_text='Name of the category.')
    imgpath = models.CharField(max_length=100 ,blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    # Model for representing contact informations of courses
    type_of = models.IntegerField(
        choices=[
            (1, 'PHONE'),
            (2, 'FACEBOOK'),
            (3, 'EMAIL'),
        ],
        help_text='Contact info.'
    )
    value = models.CharField(max_length=100)

    def __str__(self):

        return self.value

class Branch(models.Model):
    latitude = models.CharField(max_length=100, help_text='Latitude')
    longitude = models.CharField(max_length=100, help_text='Longitude')
    address = models.CharField(max_length=150, help_text='Address')

    def __str__(self):
        return self.address

class Course(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the course')
    description = models.TextField(max_length=300, help_text='Description of the course')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    logo = models.CharField(max_length=100, blank=True, null=True)
    contacts = models.OneToOneField(Contact, on_delete=models.CASCADE)
    branches = models.OneToOneField(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
