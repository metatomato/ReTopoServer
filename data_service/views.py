from django.shortcuts import render
import os
from django.http import HttpResponse

# Create your views here.
def view_data(request):
    current_path = os.path.dirname(__file__)
    topo_path = os.path.join(current_path,'static/media/topo/kyoto.topo')
    with open (topo_path, "r") as myfile:
        topo=myfile.read().replace('\n', '')
    response = "jsonCallback("+topo+");"
    return HttpResponse(response, content_type="application/json")