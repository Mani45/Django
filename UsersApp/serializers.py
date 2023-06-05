from rest_framework import serializers
from UsersApp.models import Users,Strategies


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users 
        fields=('UserId','UserName','Email','Password','Phone','DateOfCreation')

class StrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Strategies
        fields=('id','sName','symbol','entryType','orderType') 