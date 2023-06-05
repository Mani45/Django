from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#from DjangoAPI.usersapp.models import Strategies

from UsersApp.models import Users,Strategies

from UsersApp.serializers import UsersSerializer,StrategiesSerializer

# Create your views here.

@csrf_exempt
def UsersAPI(request,id=0):
    if request.method=='GET':
        users=Users.objects.all()
        users_serializer=UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)    

@csrf_exempt
def LoginAPI(request,id=0):
 if request.method=='GET':
        print('uname-->'+ request.GET.get("username"))
        login_data=Users.objects.filter(UserName=request.GET.get("username"),Password=request.GET.get("password"))
        login_serializer=UsersSerializer(login_data,many=True)
        return JsonResponse(login_serializer.data,safe=False)

@csrf_exempt
def strategiesAPI(request,id=0):
    if request.method=='GET':
        strategies=Strategies.objects.all()
        #strategies=Strategies.objects.filter(sName='9.20')
        strategies_serializer=StrategiesSerializer(strategies,many=True)
        print("strategies_serializer-->"+str(strategies_serializer))
        return JsonResponse(strategies_serializer.data,safe=False) 
    elif request.method=='POST':
        strategy_data=JSONParser().parse(request)
        strategies_serializer=StrategiesSerializer(data=strategy_data)
        print("strategies_serializer-->"+str(strategies_serializer))
        print("strategies_serializer res-->"+str(strategies_serializer.is_valid()))
        print("strategies_serializer err-->"+str(strategies_serializer.errors))

        if strategies_serializer.is_valid():
            strategies_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

@csrf_exempt
def updateStrategy(request,id=0):
    if request.method=='PATCH':
        strategy_data=JSONParser().parse(request)
        strategies_serializer=StrategiesSerializer(data=strategy_data)
        rowNumber = strategy_data['id']
        sName = strategy_data['sName']
        print("sName-->"+str(sName))
        strategy = Strategies.objects.get(id = rowNumber)
        print("strategy-->"+str(strategy))
        strategy.save()
        return JsonResponse("Updated Successfully",safe=False)
    
@csrf_exempt
def deleteStrategy(request,id=0):
    if request.method=='PATCH':
        strategy_data=JSONParser().parse(request)
        strategies_serializer=StrategiesSerializer(data=strategy_data)
        print("sName-->"+str(strategies_serializer))
        rowNumber = strategy_data['id']
        print("number-->"+str(rowNumber))
        strategy = Strategies.objects.get(id = rowNumber)
        print("strategy-->"+str(strategy))
        #strategies=Strategies.objects.all()[rowNumber]
        #print("strategies-->"+str(strategies))
        strategy.delete()
        return JsonResponse("Deleted Successfully",safe=False)
        
         
        
