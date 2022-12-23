
from django.urls import path
from .views import Lesson_Detail, subjecte_List, subject_detail, contents, control_panel, base_nav
from django.conf import settings
from django.conf.urls.static import static

app_name = 'student'

urlpatterns = [

    path('subject', subjecte_List.as_view(), name='subject'),
    path('subject/<int:pk>', subject_detail.as_view(), name='subject_detail'),
    path('contents', contents, name='contents'),
    path('base_nav', base_nav, name='base_nav'),
    path('control_panel', control_panel, name='control_panel'),
    # path('lesson_list', Lessons_List.as_view(), name='lesson_list'),
    path('lesson_list/<int:pk>', Lesson_Detail.as_view(), name='lesson_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
