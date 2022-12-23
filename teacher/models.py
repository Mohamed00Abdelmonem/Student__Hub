from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Lesson (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='videos/%y/%m/%d')
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)



    def __str__(self):
        return self.name





# class Admin(models.Model):
#     # id = models.AutoField(primary_key=True)
#     name_teacher = models.CharField(max_length=200)
#     phone_teacher = models.IntegerField()
#     password_teacher = models.CharField(max_length=200)
#     code_teacher = models.IntegerField()
#     subject = models.ForeignKey(subject, on_delete=models.DO_NOTHING)
    #
    # def __str__(self):
    #     return self.name






class Student(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    password = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name
