from django.shortcuts import render
from django.shortcuts import get_object_or_404 as _get_object_or_404

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView

from books.serializers import BookSerializer
from books.models import Books

# Create your views here.
class BooksView(APIView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'PATCH', 'GET')

    def post(self, request, *args, **kwargs):
        #request.META.get('REMOTE_ADDR')
        return BookPost.as_view()(request._request)

    def get(self, request, *args, **kwargs):
        return BookGet.as_view()(request._request)

    def patch(self, request, *args, **kwargs):
        return BookUpdate.as_view()(request._request)

    def put(self, request, *args, **kwargs):
        return Response({'ERROR':'method PUT not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        return Response({'ERROR':'method DELETE not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class BookPost(CreateAPIView):

    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        print("Inside book post serializers")
        return BookSerializer

    def post(self, request, *args, **kwargs):
        return super(BookPost, self).post(request, *args, **kwargs)

def get_object_or_404(queryset, *filter_args, **filter_kwargs):
    """
    Same as Django's standard shortcut, but make sure to also raise 404
    if the filter_kwargs don't match the required types.
    """
    try:
        return _get_object_or_404(queryset, *filter_args, **filter_kwargs)
    except (TypeError, ValueError):
        raise Http404

class BookUpdate(UpdateAPIView):

    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_serializer_class(self):
        return BookSerializer

    def get_queryset(self):
        book_id = self.request.data.get('book_id')
        try:
            book_obj = Books.objects.filter(id=book_id,is_active=1)
        except:
            return Response({'ERROR': 'Invalid book_id'}, status=status.HTTP_400_BAD_REQUEST)
        return book_obj

    def patch(self,request, *args, **kwargs):
        return super(BookUpdate,self).patch(request, *args, **kwargs)

    # Dont have to serve PUT request for exposed URL 
    def put(self, request, *args, **kwargs):
        return Response({'ERROR':"Method \"PUT\" not allowed."}, status=status.HTTP_400_BAD_REQUEST)


class BookGet(ListAPIView):

    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Books.objects.all()
        #return Books.objects.all().order_by('-created')
                
    def get_serializer_class(self):
        return BookSerializer

    def get(self, request, *args, **kwargs):
        return super(BookGet, self).get(request, *args, **kwargs)


