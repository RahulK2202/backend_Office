from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [

    path('login/', AdminLoginView.as_view(), name='admin_login'),
    # path('logout/',AdminLogoutView.as_view(), name='logout'),
    path('registration/',EmployeeRegistrationView.as_view(), name='registration/'),
    #  path('send_email_to_employee',send_email_to_employee, name='registration/'),
    path('userlogin/', LoginView.as_view(), name='login'),
    path('verify-token/',verify_token, name='verify_token'),
    path('employelist/',EmployeeListView.as_view(), name='employelist'),
    path('blockemployees/<int:employee_id>/', BlockEmployeeView.as_view(), name='block_employee'),
    path('unblockemployees/<int:employee_id>/', UnblockEmployeeView.as_view(), name='unblock_employee'),
    # path('edit/<int:employee_id>/', EmployeeEditView.as_view(), name='employee-edit'),
    path('edit/<int:pk>/', EmployeeEditView.as_view(), name='employeee-detail'),
    path('details/<int:pk>/', EmployeeEditView.as_view(), name='details'),
    path('departments/', DepartmentListAPIView.as_view(), name='departments'),
    path('departments/<int:pk>/', DepartmentListAPIView.as_view(), name='department_detail'),

    path('departments/<int:pk>/', DepartmentListAPIView.as_view(), name='department-update'),

    path('changepass/', ChangePass.as_view(), name='change_password'),
   
    path('announcements/', AnnouncementEditView.as_view()),

    path('announcements/<int:announcement_id>/delete/', AnnouncementEditView.as_view(), name='announcement_delete'),

    path('userdetails/<int:user_id>/', views.Employeedetails, name='userdetails'),
    
    path('upload-profile-picture/', views.upload_profile_picture, name='upload_profile_picture/'),
    # path('change/', views.GetImageView.as_view(), name='profile_picture'),
  
]


