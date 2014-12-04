from django.http import HttpResponse


def home(request):
    
    html = "<html><body>Guiseppe is my moocbuddy</body></html>" 
    return HttpResponse(html)