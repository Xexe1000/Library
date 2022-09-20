from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='image', null=True, blank=True)
    genre = models.ForeignKey('Book.Genre', models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    choice = [
        ('book', 'book'),
        ('audiobook', 'audiobook'),
    ]
    type = models.CharField(max_length=9, choices=choice, default='book')
    premium = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"



class Genre(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"



class File(models.Model):
    book = models.ForeignKey('Book', models.CASCADE, null=True, blank=True, related_name='file')
    file = models.FileField(upload_to='book_file', null=True, blank=True)

    def __str__(self):
        return f"{self.book} - {self.file}"


class Comment(models.Model):
    comment = models.ForeignKey('Book', models.CASCADE, related_name='comment', null=True)
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    text = models.TextField(max_length=255)
    comment_comment = models.ForeignKey('self', models.SET_NULL, null=True, related_name='comments_comment', blank=True)

    def __str__(self):
        return f"{self.comment} - {self.user} : {self.comment}"



class Like(models.Model):
    like = models.ForeignKey('Book', models.CASCADE, related_name='like')
    user = models.ForeignKey(User, models.CASCADE, null=True)

    def __str__(self):
        return f"{self.like} - {self.user}"


class Rating(models.Model):
    RATE_CHOICES = (
        (1, '1'), (2, '2'),
        (3, '3'), (4, '4'),
        (5, '5'), (6, '6'),
        (7, '7'), (8, '8'),
        (9, '9'), (10, '10'),
    )
    book = models.ForeignKey(Book, models.CASCADE, related_name='rate')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    star = models.FloatField('Rating', choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.star} - {self.book} by {self.user}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorite')

    def __str__(self):
        return f"{self.user} - {self.Book}"
