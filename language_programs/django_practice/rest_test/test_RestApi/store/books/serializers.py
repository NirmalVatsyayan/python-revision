from rest_framework.serializers import Serializer, ModelSerializer
from books.models import Books
import time
import datetime


class BookSerializer(ModelSerializer):
    
    def to_representation(self, obj):
        ret = super(BookSerializer,self).to_representation(obj)
        return ret

    class Meta:
        model = Books
        fields = ('id','name','author','publication','max_print','is_active',\
              'created', 'updated')