from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def single_photo(request):
	return HttpResponse('사진출력되는 부분')