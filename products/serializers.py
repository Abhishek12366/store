from rest_framework import serializers
from products.models import Mobiles

class Productserilizer(serializers.Serializer):
    name=serializers.CharField()
    brand=serializers.CharField()
    specs=serializers.CharField()
    price=serializers.IntegerField()  
class Modibileserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Mobiles
        fields="__all__"


        # fields= [
        # "name",
        # "brand",
        # "specs",
        # "price" ]
