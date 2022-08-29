from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import mobiles


class MobilesView(APIView):
    def get(self,request,*args,**kwargs):
        all_mobiles=mobiles
        # print(all_mobiles)
        # print(request.query_params)
        if "display" in request.query_params:
            disp=request.query_params.get("display")
            all_mobiles=[mobile for mobile in all_mobiles if mobile.get("display")==disp]
        if "brand" in request.query_params:
            brand=request.query_params.get("brand")
            all_mobiles=[mob for mob in all_mobiles if mob.get("brand")==brand]
        # print(all_mobiles)
        return Response({"mobiles":all_mobiles})

    def post(self,request,*args,**kwargs):
        qs=request.data
        mobiles.append(qs)
        return Response({"msg":mobiles})



class MobilesDetails(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=[mobile for mobile in mobiles if mobile.get("id")==id].pop()
        return Response({"data":data})

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=request.data
        instance=[mobile for mobile in mobiles if mobile.get("id")==id].pop()
        instance.update(data)
        return Response({"msg":mobiles})

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=[mobile for mobile in mobiles if mobile.get("id")==id].pop()
        mobiles.remove(instance)
        return Response({"deleted":instance})



