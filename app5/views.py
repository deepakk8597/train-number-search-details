from django.shortcuts import render
from django.views.generic import View
import requests

class GetTrainDetails(View):
    def get(self,request):
        return render(request,"index.html")
    def post(self,request):
        train_name = request.POST.get("t1")


        url = "https://trains.p.rapidapi.com/"

        payload = "{\"search\":\""+train_name+"\"}"
        headers = {
            'x-rapidapi-host': "trains.p.rapidapi.com",
            'x-rapidapi-key': "4422ecdd22msh0284eaac7d64721p1d830ejsn5fc033392fd1",
            'content-type': "application/json",
            'accept': "application/json"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        train_info = response.json()
        return render(request, "index.html",{"data":train_info})