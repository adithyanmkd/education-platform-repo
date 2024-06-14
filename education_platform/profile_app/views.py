from django.shortcuts import render

# Create your views here.
def profile_app(request):
    return render(request, 'html/profile-page.html')
