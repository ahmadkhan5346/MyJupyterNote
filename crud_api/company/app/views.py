from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import ContactApiSerializer
from rest_framework import status
from app.models import Contact


class StudentApi(APIView):
    def post(self, request):
        serializer = ContactApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        data = request.data
        if data:
            contact = Contact.objects.get(id=data['id'])
            serializer = ContactApiSerializer(contact)
            return Response(serializer.data)
        else:
            contact = Contact.objects.all()
            serializer = ContactApiSerializer(contact, many=True)
            return Response(serializer.data)

    def put(self, request):
        data = request.data
        contact = Contact.objects.get(id=data['id'])
        contact.name = data['name']
        contact.roll_no = data['roll_no']
        contact.city = data['city']
        contact.save()

        serializer = ContactApiSerializer(contact)
        return Response(serializer.data)
    
    def delete(self, request):
        data = request.data
        Contact.objects.get(id=data['id']).delete()
        return Response({'msg':'data deleted'})
