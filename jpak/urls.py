"""jpak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

# router functionality for Django and PersonalNoteViewSet
from rest_framework import routers
from notes.api import PersonalNoteViewSet

# (1) setting up endpoint
from graphene_django.views import GraphQLView

# Day 4 Token Auth
from rest_framework.authtoken import views

# making default router from routers package and registering the router
router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # (2) 
    path('graphql/', GraphQLView.as_view(graphiql=True)),

    # sets the path to /api/notes
    # use router.register to add as many paths without needing to add to urlpatterns
    path('api/', include(router.urls)),

    # setting up route to authenticate users // re_path interprets enpoint as regex instead of fixed string
    path('api-token-auth/', views.obtain_auth_token)
]

