from django.http import HttpResponse

def home(request):
    #print "hello world"
    #print request
    return HttpResponse("Hello World !")
