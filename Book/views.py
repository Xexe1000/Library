# from rest_framework import generics
from django.db.models import Prefetch, F, Count
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from Book.models import Book, Genre, Comment, Like
from Book.permissions import BookPermission
from Book.serializers import BookSerializer, CommentSerializer, DetailSerializer, GenreDescriptionSerializer
from django_filters import rest_framework as filters


class BookFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['genre']


class BookView(ModelViewSet):
    # queryset = Book.objects.select_related('all').all().order_by('-id')
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    serializer_classes = {
        'retrieve': DetailSerializer
    }
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_set_fields = ['genre']
    filter_set_class = BookFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price']
    permission_classes = (BookPermission,)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = Book.objects.annotate(
            genre_name=F('genre__name'),
            owner_name=F('user__username'),
            likes_count=Count('like__like'),
            comment_count=Count('comment__comment'),
        ).order_by('-id')
        return queryset


class GenreView(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreDescriptionSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Genre.objects.annotate(
            genre_count=Count('book'),
            descriptions_text=Count('description'),
        )
        return queryset


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            book_id=kwargs.get('book_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class LikeView(APIView):

    def get(self, request, book_pk):
        created = Like.objects.filter(book_id=book_pk, user=request.user).exists()
        if created:
            Like.objects.filter(
                book_id=book_pk,
                user=request.user
            ).delete()
            return Response({'success': 'unliked'})
        else:
            Like.objects.create(book_id=book_pk, user=request.user)
            return Response({'success': 'liked'})