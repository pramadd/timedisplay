# from django.conf.urls import url
# from . import views           # This line is new!
# urlpatterns = [
#     url(r'^$', views.index)     # This line has changed!
# ]


# from django.shortcuts import render, HttpResponse, redirect
# def yourMethodFromUrls(request):
#   context = {
#   "name":"reddy"
#   }
#   return render(request,'appname/page.html', context)


from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime("%B %d, %Y %H:%M:%S %p", gmtime())
  }
  return render(request,'time_display/page.html', context)