from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import shop_view

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from drf.shop.models import Categories, Books
from drf.shop.serializers import UserSerializer, GroupSerializer, CategoriesSerializer, BooksSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

 class CategoriesViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]

    class BooksViewSet(viewsets.ModelViewSet):
        queryset = Books.objects.all()
        serializer_class = BooksSerializer
        permission_classes = [permissions.IsAuthenticated]


