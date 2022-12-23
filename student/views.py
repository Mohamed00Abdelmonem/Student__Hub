# from django.shortcuts import render
# from .models import subjecte, lesson
#
# from django.views.generic import ListView, DetailView
#
#
# # Create your views here.
#
#
# def contents(request):
#     return render(request, 'student/contents.html')
#
#
# def control_panel(request):
#     return render(request, 'student/control_panel.html')
#
#
# def subject(request):
#     subjects = subjecte.objects.all()
#     context = {'subjects': subjects}
#     return render(request, 'student/subjecte_List.html', context)
#
# class Subject_List(ListView):
#     model = lesson
# #
# # class Subject_List(ListView):
# #     model = subjecte
#
#
#
# class Subject_detail(DetailView):
#     model = subjecte
#
#
# class Lesson_Detail(DetailView):
#     model = lesson







from django.shortcuts import render
from .models import subjecte, lesson
from django.views.generic import ListView, DetailView


# Create your views here.


def contents(request):
    return render(request, 'student/contents.html')

def base_nav(request):
    return render(request, 'student/base_nav.html')


def control_panel(request):
    return render(request, 'student/control_panel.html')


# def subject(request):
#   subjects = subjecte.objects.all()
#  context = {'subjects': subjects}
# return render(request, 'student/subjecte_List.html', context)


class subjecte_List(ListView):
    model = subjecte


class Lesson_Detail(DetailView):
    model = lesson


# class Lessons_List(ListView):
# model = lesson

class subject_detail(DetailView):
    model = subjecte

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subjecte = self.get_object()
        context["subject_lesson"] = lesson.objects.filter(subject=subjecte)
        return context