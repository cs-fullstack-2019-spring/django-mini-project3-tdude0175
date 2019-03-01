from django.urls import path
from . import views



urlpatterns = \
    [
        path('', views.index, name = 'index'),
        path('teacherDetails/<str:teacherID>/',views.detailList, name ='teacherDetails'),
        path('schoolDetails/<str:schoolID>/', views.schoolDetailList, name ='schoolDetails'),
        path('updateDetails/<int:classID>/', views.updateDetails , name = 'updateDetails'),
        path('DeleteEntry/<int:classID>/', views.deleteDetails, name = 'deleteEntry'),
        path('newEntry/', views.newEntry, name='newEntry'),
    ]