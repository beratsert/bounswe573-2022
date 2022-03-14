from ast import keyword
from zoneinfo import available_timezones
from django.shortcuts import render
from django.http import HttpResponse
from .models import Entries
import pywikibot

# Create your views here.
class Configuration:
    source = 'wikipedia'
    source_language = 'en'
    available_languages = ['en', 'es', 'de', 'tr', 'fr']


def home(request):
    keyword = 'monkey'
    wpsite = pywikibot.Site(Configuration.source_language, Configuration.source)
    wppage = pywikibot.Page(wpsite, keyword)
    item = pywikibot.ItemPage.fromPage(wppage) 
    dictionary = item.get()
    
    for lang in Configuration.available_languages:
        entry = Entries.objects.create(keyword = keyword, description = dictionary['descriptions'][lang], language = lang)
        entry.save()
    Entries.objects.all()
    return HttpResponse(Entries.objects.all()[1].description)
