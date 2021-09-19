from django.urls import path
from .views import uploadIamage, showImage, homepage

urlpatterns=[
    path('', homepage, name='home'),

    path('upload',uploadIamage,name='upload'),
    path('show', showImage, name='show'),

]