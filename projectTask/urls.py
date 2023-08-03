from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('individualtasks/<int:pk>/', individual_task, name='individual-task'),
    path('usertasks/<int:pk>/', views.update_task_status, name='update-task-status'),
]
