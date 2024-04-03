from django.urls import path
from .views import Home,forgot_password,ChangePassword,handle_upload,details,StudentView,Counselling,counsellor_list, CounsellorLoginAPIView
urlpatterns = [
    path('', Home),
    path('students/',StudentView.as_view()),
    path('upload/', handle_upload, name='upload'),
    path('student/',details),
    path('forgotpassword/',forgot_password),
    path('resetpassword/<token>/' , ChangePassword , name="change_password"),
    path('counsellor/',Counselling.as_view()),
    path('counsellorsList/', counsellor_list),
    #path('login/',counsellor_login),
    path('login/', CounsellorLoginAPIView.as_view(), name='counsellor-login'),

]