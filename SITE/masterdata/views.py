from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request, 'index.html', context={})


class UserView(APIView):
	#authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

	def post(self, request):
		print ("inside the view")
		return Response({})

