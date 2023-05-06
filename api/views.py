from api.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.serializers import UserSerializer


@api_view(['POST'])
def home(request):
    try :
        data = {
            "username" : "yanis",
            "age" : "young adult",
            "gender" : "male",
            "activity" : "high",
            "height" : "180",
            "weight" : "70",
            "goal" : "bulk",
            "schedule" : "busy"
        }

        result = {
            "health" : "good",
            "food" : "increase",
            "training" : "high (5 a week)",
            "program" : "arnold split",
            "eat" : ["meat","eggs","fish","vegetables","fruits"],
            "avoid" : ["nothing"],
            "nutients" : {
                "calories" : "5000",
                "protien" : "200g",
                "carbs" : "500g",
                "fibres" : "50g",
                "fat" : "60"
            },
            "advice" : ["Eat in a surplus","Lift heavy weights consistently","Get enough rest and recovery"]
        }
    except Exception as e:
        print(e)
        return Response({'status' : 'fail','message' : 'ERROR !'},status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'status' : 'success','data' : result})

@api_view(['GET'])
def getUsers(request):

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):    
    created = False
    try :
        data  = request.data
        if User.objects.filter(username = data['username']).exists() :
            if not User.objects.filter(username= data['username'], password=data['password']).exists() :
                return Response({'status' : 'fail','message' : 'change username or password'},status=status.HTTP_400_BAD_REQUEST)
        else :
            created = True
            User.objects.create(username=data['username'], password=data['password'])

    except Exception as e:
        print(e)
        return Response({'status' : 'fail','message' : 'user not logged in'},status=status.HTTP_400_BAD_REQUEST)
    if created :
        return Response({'status' : 'success','message' : 'created', 'username':data['username']})
    else :
        return Response({'status' : 'success','message' : 'logged in', 'username':data['username']})