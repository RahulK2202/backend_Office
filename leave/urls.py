from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [

   
path('leaves/', LeaveApplicationView.as_view(), name='leave-application'),
path('dashboard_data/', views.DashboardDataAPIView.as_view(), name='dashboard_data'),
path('userleave/<int:employee_id>/', UserLeaveDataView.as_view(), name='user-leave-data'),
path('employee_leave_requests/<int:employee_id>/', get_employee_leave_requests),

 
]