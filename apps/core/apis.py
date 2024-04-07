from apps.core.models import Division, District, Upazila, PostCode
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from apps.core.utils import api_success, api_error


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Division
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model  = District
        fields = '__all__'


class UpazilaSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model  = Upazila
        # fields = '__all__'
        fields = [
            'id', 'name', 'bn_name', 'lat', 'long', 'district', 'created_at', 'updated_at'
        ]

    def get_name(self, instance):
        return f"{instance.name} ({instance.bn_name})"


class PostCodeSerializer(serializers.ModelSerializer):
    postCode = serializers.SerializerMethodField()
    postOffice = serializers.SerializerMethodField()

    class Meta:
        model = PostCode
        fields = [
            'id', 'division', 'district', 'postCode', 'postOffice', 'upazila', 'created_at', 'updated_at'
        ]

    def get_postCode(self, instance):
        post_code = str(instance.postCode)
        return post_code.split(".")[0]
    
    def get_postOffice(self, instance):
        post_code = str(instance.postCode)
        data = f"{instance.upazila}, {instance.postOffice}-{post_code.split('.')[0]}"
        return data


class DivisionList(generics.ListAPIView):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        msg = {
                "total": queryset.count(),
                "message": "Division List"
            }
        return api_success(serializer.data, status=200, message=msg)



class DistrictList(APIView):
    serializer_class = DistrictSerializer
    
    def get(self, request, pk=None): 
        try:
            if pk is not None:
                division = Division.objects.get(pk=pk)
                districts = District.objects.filter(division=division)
            else:
                districts = District.objects.all()
            
            serializer = self.serializer_class(districts, many=True)
            msg = {
                "total": districts.count(),
                "message": "District List."
            }
            return api_success(serializer.data, status=200, message=msg)

        
        except Division.DoesNotExist:
            return api_error({'errors': "Division not found"}, status=404, message="Not Found!")
        except Exception as e:
            return api_error({'errors': str(e)}, status=500, message="Internal Server Error!")




class UpazilaList(APIView):
    serializer_class = UpazilaSerializer
    
    def get(self, request, pk=None):
        try:
            if pk is not None:
                district = District.objects.get(pk=pk)
                upazilas = Upazila.objects.filter(district=district)
            else:
                upazilas = Upazila.objects.all()
            
            serializer = self.serializer_class(upazilas, many=True)
            msg = {
                "total": upazilas.count(),
                "message": "Upazila List."
            }
            return api_success(serializer.data, status=200, message=msg)

        
        except District.DoesNotExist:
            return api_error({'errors': "District matching query does not exist."}, status=404, message="Not Found!")
        except Exception as e:
            return api_error({'errors': str(e)}, status=500, message="Internal Server Error!")






class PostCodeList(APIView):
    serializer_class = PostCodeSerializer
    
    def get(self, request, division_id=None, district_id=None):
        try:
            # if division_id is not None:
            #     division = Division.objects.get(pk=division_id)
            #     postcode = PostCode.objects.filter(division=division)
            if district_id is not None:
                district = District.objects.get(pk=district_id)
                postcode = PostCode.objects.filter(district=district)
            else:
                postcode = PostCode.objects.all()
            
            serializer = self.serializer_class(postcode, many=True)
            msg = {
                "total": postcode.count(),
                "message": "Post Code List."
            }
            return api_success(serializer.data, status=200, message=msg)
        
        except ObjectDoesNotExist as e:
            return api_error({'errors': str(e)}, status=404, message="Not Found!")
        except Exception as e:
            return api_error({'errors': str(e)}, status=500, message="Internal Server Error!")

