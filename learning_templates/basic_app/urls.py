from django.urls import path, include
# Instead of basic_app could be rerplaced with . (means current directory)
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
