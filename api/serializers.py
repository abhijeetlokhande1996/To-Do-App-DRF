from api.models import ToDoModel
from rest_framework.serializers import ModelSerializer

class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDoModel
        fields = '__all__'
