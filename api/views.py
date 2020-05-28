from api.serializers import ToDoSerializer
from api.models import ToDoModel
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class ToDoViewSet(ModelViewSet):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer
