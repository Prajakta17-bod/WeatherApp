from django.shortcuts import render
from django.contrib import messages
import requests
import json
import datetime
import os



def home(request):
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'Indore'     
    
    appid_value= os.environ.get('appid')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid_value}'
    PARAMS = {'units':'metric'}

    API_KEY_value = os.environ.get('API_KEY')
    SEARCH_ENGINE_ID=os.environ.get('SEARCH_ENGINE_ID')

    

    query = city
    page = 1
    start = (page - 1)* 10 + 1
    searchType = 'image'

    city_url=f"https://www.googleapis.com/customsearch/v1?key={API_KEY_value}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"


    data = requests.get(city_url).json() 
    count = 1
    search_items = data.get("items")
    image_url = search_items[0]['link']
    

    try:
          


          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          # city = 'indore'
          # data = requests.get(url,params=PARAMS).json()
          
          # description = data['weather'][0]['description']
          # icon = data['weather'][0]['icon']
          # temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )
          
