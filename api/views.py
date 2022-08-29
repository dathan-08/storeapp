
from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# # Create your views here.
#
# class MyView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"Hello World"}) #clientine json file aayit response pookum
from rest_framework.views import APIView
from rest_framework.response import Response

class MyView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Hello world"})

class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Morning"})

class GoodAfternoonView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Afternoon"})

class GoodEveningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good Evening"})

class AddViews(APIView):
    def post(self,request,*args,**kwargs):
        print("here")
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response({'msg':res})
class SubViews(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response({"msg":res})

class Factorialviews(APIView):
    def post(self,request,*args,**kwargs):
        fact=1
        num1=request.data.get("num")
        for i in range(1,num1+1):
            fact=fact*i
        return Response({"result":fact})

