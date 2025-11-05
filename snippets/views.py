from django.shortcuts import render
from .models  import Snippets
from django.http import HttpResponse ,Http404 #,JsonResponse 
from snippets.serializers import SnippetSerializer
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


"""
#@api_view(["GET","POST"])
class SnippetsList(APIView):
    def get(self, request ,  format = None):
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many = True)
        return Response(serializer.data )

    def post(self, request, format = None):
        serializer =SnippetSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status = status.HTTP_201_CREATED) 
        return  Response(serializer.errors,  status= status.HTTP_400_BAD_REQUEST) 

#@api_view(["GET","PUT","DELETE"])
class SnippetDetails(APIView):

    def get_object(self , pk ):
        try:
            return Snippets.objects.get(pk =pk)
        except Snippets.DoesNotExist: 
            raise Http404
    
    def get(self , request , pk , format = None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    def put(self , request , pk ,format = None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk ,format = None):
        snippet = self.get_object(pk)
        snippet.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)

"""    


"""
class SnippetsList(mixins.ListModelMixin , mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer

    def get(self , request, *args , **kwargs):
        return self.list(request,  **args , **kwargs)
    
    def post(self , request , *args, **kwargs):
        return self.create(request , **args, **kwargs)
    
class SnippetsDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin , 
    generics.GenericAPIView):
    
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer

    def get(self , request,  *args , **kwargs):
        return self.retrieve(request,  **args , **kwargs)
    
    def put(self , request , *args, **kwargs):
        return self.update(request , **args, **kwargs)
    
    def put(self , request , *args, **kwargs):
        return self.destroy(request , **args, **kwargs)
"""

class SnippetsList(generics.ListCreateAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer
    
class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer