from rest_framework import serializers
from Book.models import Book, Genre, Comment, Like, File, Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }


class GenreDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name', 'pk', 'description']
        extra_kwargs = {
            'user': {'read_only': True},
        }


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name', 'pk']
        extra_kwargs = {
            'user': {'read_only': True},
        }


class BookSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField()
    genre_name = serializers.CharField()
    likes_count = serializers.IntegerField()
    owner_name = serializers.CharField(read_only=True)
    rate = RatingSerializer(many=True)
    rating_count = serializers.IntegerField(read_only=True)
    _average_rating = serializers.DecimalField(read_only=True, max_digits=4, decimal_places=2)

    class Meta:
        model = Book
        fields = (
            'id', 'name', 'price', 'image', 'genre_name', 'owner_name', '_average_rating',
            'comment_count', 'type', 'likes_count', 'rate', 'rating_count',
        )
        extra_kwargs = {'user': {'read_only': True}}


class DetailSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField()
    comment = CommentSerializer(many=True)
    likes_count = serializers.IntegerField()
    file = FileSerializer(many=True)
    owner_name = serializers.CharField(read_only=True)
    rate = RatingSerializer(many=True)
    rating_count = serializers.IntegerField(read_only=True)
    _average_rating = serializers.DecimalField(read_only=True, max_digits=4, decimal_places=2)

    class Meta:
        model = Book
        fields = (
            'id', 'name', 'price', 'description', 'image', 'genre_name', 'rate', 'rating_count',
            'file', 'comment', 'likes_count', 'type', 'owner_name', '_average_rating',
        )
        extra_kwargs = {'user': {'read_only': True}}
