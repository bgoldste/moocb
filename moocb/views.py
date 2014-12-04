from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    
    # html = "<html><body>Guiseppe is my moocbuddy</body></html>" 
    # return HttpResponse(html)
    return render_to_response('moocb/home.html')




