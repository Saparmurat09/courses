from coursesapp import views

from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
