from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name


        from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

  


# NEW MODULE (Course)
class Course(models.Model):
    title = models.CharField(max_length=200)
    duration = models.IntegerField()
    fee = models.IntegerField()

    def __str__(self):
        return self.title

