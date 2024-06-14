from django.shortcuts import render

# Create your views here.
def tutorial(request):
    return render(request, 'html/tutorial.html')

def playlist(request):
    return render(request, 'html/playlist-page.html')