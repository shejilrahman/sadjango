from django.db import models

class Division(models.Model):
    name_of_division=models.CharField(max_length=200)
    division_office_number=models.CharField(max_length=15)
    def __str__(self):
        return self.name_of_division


class Member(models.Model):
    Type = models.TextChoices('Type', 'SA OA')
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    working_as=models.CharField(default='SA',choices=Type.choices,max_length=60)
    phonenumber= models.CharField(max_length=15)
    remarks=models.CharField(max_length=300,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name