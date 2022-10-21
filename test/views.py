from django.shortcuts import render
from django.http import HttpResponse
import random

def url():
  cap = "abcdefghijklmnopqrstuvwxyz"
  sml = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  num = "0123456789"
  ans = cap + sml + num 
  leng = 5
  url = "".join(random.sample(ans,leng))
  print(url)
# Create your views here.
def home(request):
  return HttpResponse("<h1>Hellow world</h1>")
