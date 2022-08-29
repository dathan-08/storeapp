from rest_framework import serializers
from mobapi.models import Mobiles



#for REFERENCE
# ///////////////////////////
class MobileSeriliazer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    band=serializers.CharField()
    display=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()
# /////////////////////////////



class MobileModelSerilizer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Mobiles
        fields="__all__"
        #fields=["name","brand","display","price","rating"]