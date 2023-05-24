from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import requests 
import json
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.
# def nlp(request): 
#     return HttpResponse("Hello World!")

def landing(request): 
    template = loader.get_template("landing.html")
    return HttpResponse(template.render())

def frequencies(request): 
    template = loader.get_template("frequencies.html")
    return HttpResponse(template.render())

def summarization(request): 
    template = loader.get_template("summarization.html")
    return HttpResponse(template.render())

def lang_detection(request): 
    template = loader.get_template("lang_detection.html")
    return HttpResponse(template.render())

def keywords(request): 
    template = loader.get_template("keywords.html")
    return HttpResponse(template.render())
    
@csrf_exempt    
def get_language(request):
    if request.method == 'POST':
        text = request.POST.get('text-field', '')  # entered text from the form
        endpoint = "http://localhost:8082/detect_lang"
        data = {"text": text}
        response = requests.post(url=endpoint, json=data)
        response_dict = json.loads(response.content)
        language = response_dict["Language"]
        return JsonResponse({"language": language}) 
    else:
        pass

@csrf_exempt    
def get_keywords(request):
    if request.method == 'POST':
        text = request.POST.get('text-field', '')  # entered text from the form
        endpoint = "http://localhost:8082/kwords"
        data = {"text": text}
        response = requests.post(url=endpoint, json=data)
        response_dict = json.loads(response.content)
        keywords = [" " + word for word in response_dict["Keywords"]]
        return JsonResponse({"keywords": keywords}) 
    else:
        pass

@csrf_exempt    
def get_freq_dict(request):
    if request.method == 'POST':
        text = request.POST.get('text-field', '')  # entered text from the form
        endpoint = "http://localhost:8082/freq_dict"
        data = {"text": text}
        response = requests.post(url=endpoint, json=data)
        response_dict = json.loads(response.content)["Frequencies"]
        print(response_dict)
        freqs = ""
        for item in response_dict:
            string = item[0] + ": " + str(item[1]) + ", "
            print(string)
            freqs += string

        return JsonResponse({"frequencies": freqs}) 
    else:
        pass

@csrf_exempt    
def get_summary(request):
    if request.method == 'POST':
        text = request.POST.get('text-field', '')  # entered text from the form
        endpoint = "http://localhost:8082/summarize"
        data = {"text": text}
        response = requests.post(url=endpoint, json=data)
        summary = json.loads(response.content)["Summary"]

        return JsonResponse({"summary": summary}) 
    else:
        pass