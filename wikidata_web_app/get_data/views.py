from ast import keyword
from zoneinfo import available_timezones
from django.shortcuts import render
from django.http import HttpResponse
from .models import Entries, Inputs
from django.core.handlers.wsgi import WSGIRequest
import pywikibot


# Create your views here.
class Configuration:
    source = 'wikipedia'
    source_language = 'en'
    available_languages = ['en', 'es', 'de', 'tr', 'fr']

def save_obejcts(keyword: str):
    wpsite = pywikibot.Site(Configuration.source_language, Configuration.source)
    wppage = pywikibot.Page(wpsite, keyword)
    item = pywikibot.ItemPage.fromPage(wppage) 
    dictionary = item.get()
    
    for lang in Configuration.available_languages:
        try:
            entry = Entries.objects.create(keyword = keyword, description = dictionary['descriptions'][lang], language = lang)
            entry.save()
        except:
            pass

def home(request: WSGIRequest) -> HttpResponse:
    
    input_button_html = ''' 
    <h1>This is the home page for basic wikidata webservice</h1>
    <h3>Type your keyword and limit the results, page will display the results..</h3>
    <form action = "" method = "get">
    <label for="keyword">Keyword: </label>
    <input id="keyword" type="text" name="keyword">
    <input type="submit" value="OK">
    '''
    
    save_obejcts(request.GET['keyword'])

    #Entries.objects.all()
    #    return HttpResponse(Entries.objects.all()[1].description)
    #else:
    return HttpResponse(input_button_html)

def display(request: WSGIRequest) -> HttpResponse:
    output = ''
    for item in Entries.objects.all():
        output += '<p>'+item.keyword + '-' + item.language + ': ' + item.description + '</p>'
    
    return HttpResponse(output)
