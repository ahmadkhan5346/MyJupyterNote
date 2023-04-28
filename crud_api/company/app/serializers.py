from rest_framework import serializers
from app.models import Contact


class ContactApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "roll_no", "city"]