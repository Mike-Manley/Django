from django.shortcuts import render
from django.http import HttpResponse


def homePageView(requst):
    return HttpResponse('On Notes')
