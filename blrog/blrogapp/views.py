from django.shortcuts import render, get_object_or_404
from blrogapp.models import Category, Contents

# Create your views here.

def lists(request):
    latest_lists = Contents.objects.all().order_by('-date')[:8]
    context = {'latest_lists':latest_lists}
    return render(request,'blrogapp/lists.html',context)

def reading(request,content_id):
    contents = get_object_or_404(Contents,pk=content_id)
    return render(request,'blrogapp/reading.html',{'contents':contents})


