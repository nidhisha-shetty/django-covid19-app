from django.db import models

# Create your models here.
class Covid(models.Model):

	stateChoice = (('Select a state','select a state'),("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
				   ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh", "Arunachal Pradesh"), ("Assam","Assam"), ("Bihar","Bihar"), ("Chandigarh","Chandigarh"), ("Chhattisgarh","Chhattisgarh"), ("Dadra and Nagar Haveli and Daman and Diu","Dadra and Nagar Haveli and Daman and Diu"), ("Delhi","Delhi"), ("Goa","Goa"), ("Gujarat", "Gujarat"),
				   ("Haryana", "Haryana"), ("Himachal Pradesh","Himachal Pradesh"), ("Jammu and Kashmir","Jammu and Kashmir"), ("Jharkhand","Jharkhand"), ("Karnataka","Karnataka"), ("Kerala","Kerala"), ("Ladakh","Ladakh"), ("Lakshadweep","Lakshadweep"), ("Madhya Pradesh","Madhya Pradesh"), ("Maharashtra","Maharashtra"),
				   ("Manipur","Manipur"), ("Meghalaya","Meghalaya"), ("Mizoram","Mizoram"), ("Nagaland","Nagaland"), ("Odisha","Odisha"), ("Puducherry","Puducherry"), ("Punjab","Punjab"), ("Rajasthan","Rajasthan"), ("Sikkim","Sikkim"), ("Tamil Nadu","Tamil Nadu"),
				   ("Telengana","Telengana"), ("Tripura","Tripura"), ("Uttarakhand","Uttarakhand"), ("Uttar Pradesh","Uttar Pradesh"), ("West Bengal","West Bengal"))


	state=models.CharField(max_length=100, default="Maharashtra", choices=stateChoice)