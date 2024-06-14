from django.shortcuts import render

# Create your views here.
def course_selection(request):
    return render(request, 'html/course-selection.html')

def course_overview(request):
    return render(request, 'html/course-overview.html')

