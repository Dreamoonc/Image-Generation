

import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
import os

os.environ['REPLICATE_API_TOKEN']='694ef1fd05d8942f625faca24188757c054a7a42'

#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import replicate
import webbrowser

# Create your views here.

def main (request):

    #webbrowser.open(output_url)
    return render(request, 'index.html')

def create(request):
    if request.method=='POST':
        model = replicate.models.get("stability-ai/stable-diffusion")
        input= request.POST.get("textfield")
        output_url = model.predict(prompt=input)[0]

    else :
        input= request.POST.get("textfield")
        output_url=""

    return HttpResponse(output_url)



