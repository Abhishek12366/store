from urllib import request
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView 
from rest_framework.response import Response
from products import serializers
from products.models import Mobiles
from products.serializers import Productserilizer,Modibileserializer



class Productview(APIView):
    def get(self,request,*args,**kw):
        qs=Mobiles.objects.all()
        if "brand" in request.query_params:
            qs=qs.filter(brand=request.query_params.get("brand"))
        serializer=Productserilizer(qs,many=True)
        return Response(data=serializer.data)


    def post(self,request,*args,**kw):
        serializer=Modibileserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


        # serializer=Productserilizer(data=request.data)
        # if serializer.is_valid():
        #     Mobiles.objects.create(**serializer.validated_data)#unpacking
        #     return Response(data="mobile data created")
        # else:
        #     return Response(data=serializer.errors)

class Productdetailview(APIView):
    def get(self,response,*args,**kw):
        id=kw.get("id")
        qs=Mobiles.objects.filter(id=id)
        serializer=Productserilizer(qs,many=True)
        return Response(serializer.data)

    def delete(self,responce,*args,**kw):
        id=kw.get("id")
        Mobiles.objects.filter(id=id).delete()
        return Response(data="sucessfully deleted")

    def put(self,request,*args,**kw):
        id=kw.get("id")
        obj=Mobiles.objects.get(id=id)
        serializer=Modibileserializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



        # id=kw.get("id")
        # serializer=Productserilizer(data=request.data)
        # if serializer.is_vaild():
        #     Mobiles.objects.filter(id=id).update(**serializer.validated_data)
        #     return Response(data=serializer.data)
        # else:
        #     return Response(data=serializer.errors)