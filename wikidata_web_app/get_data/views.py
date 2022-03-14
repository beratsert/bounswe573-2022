from django.shortcuts import render
from django.http import HttpResponse
import pywikibot

# Create your views here.

def home(request):
    wpsite = pywikibot.Site('en', 'wikipedia')
    wppage = pywikibot.Page(wpsite, 'basketball')
    item = pywikibot.ItemPage.fromPage(wppage) 
    dictionary = item.get()
    eng_description = dictionary['descriptions']['en']
    return HttpResponse(eng_description)
