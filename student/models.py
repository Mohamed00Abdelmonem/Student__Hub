from django.db import models

# Create your models here.


class subjecte(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class lesson (models.Model):
    name_lesson = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='videos/%y/%m/%d')
    subject = models.ForeignKey(subjecte, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name_lesson


class student(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    password = models.CharField(max_length=200)
    subject = models.ForeignKey(subjecte, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name



