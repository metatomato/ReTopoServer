from django.shortcuts import render
import os
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.
def view_data(request):
    response = HttpResponseForbidden()
    if 'callback' in request.GET:
        callback = request.GET['callback']
        if callback == 'topoRequest':
            current_path = os.path.dirname(__file__)
            topo_path = os.path.join(current_path,'static/media/topo/kyoto.topo')
            with open(topo_path, "r") as myfile:
                topo = myfile.read().replace('\n', '')
            response_data = callback + "("+topo+");"
            response = HttpResponse(response_data, content_type="application/json")

    return response