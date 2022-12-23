from django.shortcuts import render

# Create your views here.


def contents_teacher(request):
    return render(request, 'teacher/contents_teacher.html')



def control_panel(request):
    return render(request, 'teacher/control_panel.html')

def exames(request):
    return render(request, 'teacher/exames.html')


def exam_google(request):
    return render(request, 'teacher/exam_google.html')