from django.contrib import admin
from .models import student, subjecte, lesson
# Register your models here.
admin.site.site_header='STUDENT HUB'
admin.site.site_title = 'STUDENT_HUB'

admin.site.register(student)
admin.site.register(subjecte)
admin.site.register(lesson)
