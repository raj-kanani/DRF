from django.urls import path
from . import views

urlpatterns = [
    # CRUD API_VIEW decorator
    path('add/', views.AddApi, name='add'),
    path('show/', views.ShowApi, name='show'),
    path('update/<int:pk>/', views.UpdateApi, name='update'),
    path('delete/<int:pk>/', views.DeleteApi, name='delete'),

    # CRUD generic class based
    path('add2/', views.AddApi2.as_view(), name='add2'),
    path('show2/', views.ShowApi2.as_view(), name='show2'),
    path('update2/<int:pk>/', views.UpdateApi2.as_view(), name='update2'),
    path('delete2/<int:pk>/', views.DeleteApi2.as_view(), name='delete2'),

    # CRUD with mixin
    path('add3/', views.AddApi3.as_view(), name='add3'),
    path('show3/', views.ShowApi3.as_view(), name='show3'),
    path('update3/<int:pk>/', views.UpdateApi3.as_view(), name='update3'),
    path('delete3/<int:pk>/', views.DeleteApi3.as_view(), name='delete3'),
    path('retrieve3/<int:pk>/', views.RetrieveApi3.as_view(), name='retrieve3'),

    # CRUD with concreate view class
    path('lc/', views.ListCreateApi.as_view(), name='lc'),
    path('rud/<int:pk>/', views.GetputdeleteApi.as_view(), name='rud'),

]
