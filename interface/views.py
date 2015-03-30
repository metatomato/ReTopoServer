from django.shortcuts import render

# Create your views here.

def view_home(request):
    print('REGULAR REQUEST')
    print('Raw Data: "%s"' % request.path)
    return render(request,'default.html')
