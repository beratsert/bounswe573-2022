from ast import keyword
from django.shortcuts import render
from django.http import HttpResponse
from .models import Entries
import pywikibot

# Create your views here.

def home(request):
    wpsite = pywikibot.Site('en', 'wikipedia')
    wppage = pywikibot.Page(wpsite, 'basketball')
    item = pywikibot.ItemPage.fromPage(wppage) 
    dictionary = item.get()
    eng_description = dictionary['descriptions']['en']
    entry1 = Entries.objects.create(keyword = 'basketball', description = eng_description, language = 'en')
    entry1.save()
    return HttpResponse(entry1.description)
