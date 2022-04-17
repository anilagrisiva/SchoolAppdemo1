from django.urls import path
from admissions.views import addNewAdmision
from admissions.views import admisuccess
from admissions.views import addNewTeacher,getStaffDetails,getoneStaff,addStaff,updateStaff,deleteStaff,sendsms


urlpatterns = [
    path('traila/',sendsms),
    path('getadm/',addNewAdmision),
    path('status/',admisuccess),
    path('newcbv/',addNewTeacher.as_view()),
    path('staffDetails/',getStaffDetails.as_view(),name='teachersList'),
    path('staff/<int:PK>/',getoneStaff.as_view()),
    path('addStaff1/',addStaff.as_view()),
    path('updateTeacher/<int:pk>/',updateStaff.as_view()),
    path('deleteTeacher/<int:pk>/',deleteStaff.as_view()),
]
