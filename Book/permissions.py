from django.contrib.auth.models import AnonymousUser

from rest_framework import permissions


class BookPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            if obj.user == request.user:
                return True

