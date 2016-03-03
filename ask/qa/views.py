from django.shortcuts import render
from django.http import HttpResponse, Http404


def bad_route(requset, *args, **kwargs):
    return Http404


def test(request, *args, **kwargs):
    return HttpResponse('OK')

