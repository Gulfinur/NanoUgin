from django.shortcuts import render
from .models import DeviceType, All_Parameters
from django.http import HttpResponseRedirect, HttpResponseNotFound
  
# получение данных из бд
def index(request):
    All_Parameters = All_Parameters.objects.all()
    return render(request, "index.html", {"All_Parameterss": All_Parameterss})
 
# добавление данных из бд
def create(request):
    create_types()  # добавляем начальные данные для компаний
 
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        All_Parameters = All_Parameters()
        All_Parameters.SN = request.POST.get("name")
        All_Parameters.Controlled = request.POST.get("price")
        All_Parameters.DeviceType_id = request.POST.get("DeviceType")
        All_Parameters.save()
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    types = DeviceType.objects.all()
    return render(request, "create.html", {"companies": companies})
 
# изменение данных в бд
def edit(request, id):
    try:
        All_Parameters = All_Parameters.objects.get(id=id)
 
        if request.method == "POST":
            All_Parameters.SN = request.POST.get("name")
            All_Parameters.Controlled = request.POST.get("price")
            All_Parameters.DeviceType_id = request.POST.get("DeviceType")
            All_Parameters.save()
            return HttpResponseRedirect("/")
        else:
            companies = DeviceType.objects.all()
            return render(request, "edit.html", {"All_Parameters": All_Parameters, "companies": companies})
    except All_Parameters.DoesNotExist:
        return HttpResponseNotFound("<h2>All_Parameters not found</h2>")
     

