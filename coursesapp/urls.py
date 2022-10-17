from coursesapp import views

from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register(r'courses/', views.CourseList.as_view(), basename='Course')
# router.register(r'courses/<int:pk>', views.CourseDetail.as_view(), basename='Course')

urlpatterns = [
    # path('',include(router.urls)
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
