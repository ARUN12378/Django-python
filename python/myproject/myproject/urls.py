from django.contrib import admin
from django.urls import path
from app1.views import create_student, get_students, get_student, update_student, delete_student
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/create-student/', create_student),
    path('api/students/', get_students),
    path('api/student/<int:id>/', get_student),
    path('api/update/<int:id>/', update_student),
    path('api/delete/<int:id>/', delete_student),
     path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
