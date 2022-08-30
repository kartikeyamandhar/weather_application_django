from django.shortcuts import render
import requests
import datetime
import threading
from django.http import HttpResponse
from django.core.paginator import Paginator
from weatherapp.models import weatherApp
from django.contrib.auth.decorators import login_required

# index function is divided into two parts, one functionality has been added,
# if you search for a city apart from the 30 cities, then the html will render only that,
# if none is entered, all 30 cities data will be rendered
#decorator for login requirement
@login_required
def index(request):

    #list for which data is required 
    city_list = ['Mumbai','Delhi','Bangalore','Hyderabad','Ahmedabad','Chennai','Kolkata','Surat','Kanpur',
                  'Pune','Jaipur','Indore','Bhopal','Agra','Amritsar','Srinagar','Jodhpur','Ranchi','Ludhiana',
                  'Kochi','Noida','Ajmer','Gurugram','Dehradun','Chandigarh','Shimla','Udaipur','Panjim','Mangalore','Vellore']

    
    searched_list = []

    #extracting data for searched city
    if 'city' in request.POST:
        all = weatherApp.objects.all()
        all.delete()
        city = request.POST['city']
        appid = '325766931b7ba75cfbcd072524284bca'
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        PARAMS={'q':city,'appid':appid,'units':'metric'}
        r = requests.get(url=URL,params = PARAMS)
        res = r.json()
        description = res['weather'][0]['description']
        temp = res['main']['temp']
        day = datetime.date.today()
        description = {city:{day:{temp:description}}}
        data = weatherApp(
            city = city,
            day = day,
            temp = temp,
            desc = description,
        )
        searched_list.append(data)
        for i in searched_list:
            i.save()
        all_searched_tasks = weatherApp.objects.all()
        return render(request,'weatherapp/index.html',{'all_tasks':all_searched_tasks})
        
    else:
        #extracting data for list of 30 cities
        res_list=[]
        all = weatherApp.objects.all()
        all.delete()

        for i in city_list:
            appid = '325766931b7ba75cfbcd072524284bca'
            URL = 'https://api.openweathermap.org/data/2.5/weather'
            PARAMS={'q':i,'appid':appid,'units':'metric'}
            r = requests.get(url=URL,params = PARAMS)
            res = r.json()
            description = res['weather'][0]['description']
            temp = res['main']['temp']
            day = datetime.date.today()
            description = {i:{day:{temp:description}}}
            data = weatherApp(
                city = i,
                day = day,
                temp = temp,
                desc = description,
            )
            res_list.append(data)
            for i in res_list:
                i.save()
            
        all_tasks = weatherApp.objects.all()
        #paged into pages of 6 entries each
        paginator = Paginator(all_tasks, 6)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
    
    return render(request,'weatherapp/index.html',{'all_tasks':all_tasks})

    

    
    


    

    
    


    