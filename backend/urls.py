from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('adminapp.urls')), 
    path('', include('userapp.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ="token_obtain_pair"),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path('', include('visitor.urls')),
    path('complaint/', include('complaints.urls')),
    path('project/', include('projectTask.urls')),
    path('leave/', include('leave.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
