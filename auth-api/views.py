from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework import status, views, viewsets, permissions
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


class RegistrationView(CreateAPIView):
    """
    Create user endpoint
    """
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class LoginView(views.APIView):

    @method_decorator(csrf_protect)
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"))

        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        serializer_context = {
            'request': request,
        }
        
        login(request, user)
        return Response(UserSerializer(user).data)


class LogoutView(views.APIView):

    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

        
class UserViewSet(viewsets.ModelViewSet):
	"""
	API Endpoint that allows users to be viewed or edited
	"""
	permission_classes = (permissions.IsAuthenticated,)
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

