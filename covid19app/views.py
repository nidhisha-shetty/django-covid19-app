from django.shortcuts import render
from .forms import CovidForm
import requests
import json
from django.contrib import messages 

data=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
data_text=json.loads(data.text)
di={"Andaman and Nicobar Islands":0, "Andhra Pradesh":1, "Arunachal Pradesh":2, "Assam":3, "Bihar":4, "Chandigarh":5, "Chhattisgarh":6, "Dadra and Nagar Haveli and Daman and Diu": 7, "Delhi":8, "Goa":9, "Gujarat":10,
"Haryana":11, "Himachal Pradesh": 12, "Jammu and Kashmir": 13, "Jharkhand":14, "Karnataka":15, "Kerala":16, "Ladakh":17, "Lakshadweep":18, "Madhya Pradesh":19, "Maharashtra":20,
"Manipur":21, "Meghalaya":22, "Mizoram":23, "Nagaland":24, "Odisha":25, "Puducherry":26, "Punjab":27, "Rajasthan":28, "Sikkim":29, "Tamil Nadu":30,
"Telengana":31, "Tripura":32, "Uttarakhand":33, "Uttar Pradesh":34, "West Bengal":35}



def home_view(request):
	india_confirmed_cases=data_text['data']['summary']['confirmedCasesIndian']
	india_recovered_cases=data_text['data']['summary']['discharged']
	india_death_cases=data_text['data']['summary']['deaths']	
	form=CovidForm(request.POST or None)
	answer=''
	if form.is_valid():
		answer = form.cleaned_data.get('state') 
		if answer in di:
			parse_data_conf=data_text['data']['regional'][di[answer]]["confirmedCasesIndian"]
			parse_data_recovered=data_text['data']['regional'][di[answer]]["discharged"]
			parse_data_deaths=data_text['data']['regional'][di[answer]]["deaths"]

			messages.info(request, parse_data_conf)
			messages.info(request, parse_data_recovered)
			messages.info(request, parse_data_deaths)
	context={
		'answer':answer,
		'context_form':form,
		'india_confirmed_cases': india_confirmed_cases,
		'india_recovered_cases': india_recovered_cases,
		'india_death_cases': india_death_cases
	}
	return render(request, 'home.html', context)