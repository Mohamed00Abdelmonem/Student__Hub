from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path('control panel', views.control_panel, name='control_panel'),
                  path('contents_teacher', views.contents_teacher, name='contents_teacher'),
                  path('exames', views.exames, name='exames'),
                  path('exam_google', views.exam_google, name='exam_google'),


              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)