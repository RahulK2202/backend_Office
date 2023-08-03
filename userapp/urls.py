# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views


# urlpatterns = [

#     # path('login/', AdminLoginView.as_view(), name='admin_login'),

# ]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MeetingViewSet


router = DefaultRouter()
router.register(r'meetings', MeetingViewSet)

urlpatterns = [
    path('meeting/', include(router.urls)),
]
