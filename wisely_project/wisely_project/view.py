from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

__author__ = 'tmehta'


def index(request):
    return render(request, 'base.html')
