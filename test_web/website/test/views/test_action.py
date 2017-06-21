# -*- coding: utf-8 -*-

from django.views.decorators.http import require_http_methods
from django.shortcuts import render

@require_http_methods(["GET", "POST"])
def aaaaa(request):
    return render(request, 'test/aaaaa.html', {})


@require_http_methods(["GET", "POST"])
def bbbbb(request):
    return render(request,'test/bbbbb.html', {})


@require_http_methods(["GET", "POST"])
def ccccc(request):
    return render(request,'test/ccccc.html', {})


@require_http_methods(["GET", "POST"])
def ddddd(request):
    return render(request,'test/ddddd.html', {})


@require_http_methods(["GET", "POST"])
def eeeee(request):
    return render(request,'test/eeeee.html', {})
