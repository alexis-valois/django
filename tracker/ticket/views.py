from django.http import HttpResponse

def home(request, name=None):
    #print "hello world"
    #print request
    if name:
        return HttpResponse("Hello %s " % name)
    else:
        return HttpResponse("Hello World !")
