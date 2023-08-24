from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from rest_framework.permissions import AllowAny
from .models import *
from datetime import datetime



class Registerview(APIView):
    def get(self,request):
        user1=User.objects.all()
        serializer=UserSerializer(user1,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class Loginview(APIView):
    def post(self , request):
        email=request.data['email']
        password=request.data['password']

        user=User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("user not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("incorrect password")
        
        return Response(
            {
                'message':'success'
            }
        )
        
        """payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token=jwt.encode(payload , 'secret' , algorithm='HS256')

        return Response({
            'jwt':token
        })"""

class DataListView(APIView):
        def get(self , request):
            from_date = request.GET.get('from_date')
            to_date = request.GET.get('to_date')
            if from_date and to_date:

                try:

                    #convert date strings to datetime objects
                    from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
                    to_date = datetime.strptime(to_date, "%Y-%m-%d").date()

    # Retrieve data based on date range
                    data = User.objects.filter(date__range=(from_date, to_date))

    # Serialize data and return 
                    serializer = UserSerializer(data, many=True)
                    return Response({'data': serializer.data})
                except ValueError as e:
                    return JsonResponse({'error': 'Invalid date format'})
            
            else:
              return JsonResponse({'error': 'Missing from_date or to_date parameters'})


    # C
            

    
    

# Create your views here.
