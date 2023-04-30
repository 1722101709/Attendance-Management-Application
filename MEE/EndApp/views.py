from django.shortcuts import render
from .models import ABC
import datetime


# Create your views here.
def home(request):
    today = datetime.date.today()
    flag = True
    flag1 = False
    today.strftime("%Y-%m-%d")
    date = today
    data = ABC.objects.filter(date=today)
    if request.method == 'POST':
        query = request.POST['query']
        date = query
        print(query)
        if ABC.objects.filter(date=query).exists():
            data = ABC.objects.filter(date=query)
        else:
            flag = False
            flag1 = True
    return render(request, 'home.html', {'data':data, 'flag':flag, 'flag1':flag1, 'date':date})