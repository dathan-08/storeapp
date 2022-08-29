from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.serializers import MobileSeriliazer,MobileModelSerilizer

from mobapi.models import Mobiles
# Create your views here.

class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all() #qsill DB query set aane varunnath
        if "name" in request.query_params:
            qs=qs.filter(name__contains=request.query_params.get("name")) #mobile name starting with 'n' (name__contains)
        if "band" in request.query_params:
            qs=qs.filter(band=request.query_params.get("band"))
        deserializers=MobileSeriliazer(qs,many=True)   #DB query set is changing to python native type by deserilazation
        return Response(data=deserializers.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileSeriliazer(data=request.data)  #changing the 'request.data' into DB query set
        if serializer.is_valid():        #checking the serializer that all objects are available in the serializer if 'name' or 'brand' or anything is missing in the serializer it will go to the else statement
            Mobiles.objects.create(**serializer.validated_data) #all datas in  'serializer' are in kwargs so thats why we used '**serializer.validated.data'
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



class MobileDetail(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        deserialization=MobileSeriliazer(qs)
        return Response(data=deserialization.data)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        mobile=Mobiles.objects.get(id=id)
        mobile.delete()
        return Response({"msg":"deleted"})

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.filter(id=id)
        data = request.data
        serializer=MobileSeriliazer(qs,data=data)

        if serializer.is_valid():
            qs.update(**serializer.validated_data)
            # qs.name=serializer.validated_data.get("name")
            # qs.brand=serializer.validated_data.get("brand")
            # qs.price=serializer.validated_data.get("price")
            # qs.band=serializer.validated_data.get("band")
            # qs.display=serializer.validated_data.get("display")
            # qs.rating=serializer.validated_data.get("rating")
            # qs.save()
            return Response({"msg":"updated"})
        else:
            return Response(data=serializer.errors)


#using the imported MobileModelSerializer class from serializer.py
class MobileModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        seriliazers=MobileModelSerilizer(qs,many=True)
        return Response(seriliazers.data)
    def post(self,request,*args,**kwargs):
        serializers=MobileModelSerilizer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        else:
            return Response(data=serializers.errors)


class MobileModelDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerilizer(qs)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerilizer(instance=qs,data=request.data) #instance=qs->which data aanne update cheyendathe
                                                                       #data=request.data->which data is updated with 'qs'
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



