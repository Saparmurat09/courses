from coursesapp import views

from django.urls import path, include

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='courses-detail'),
    path('docs/', include_docs_urls(title='Courses API', public=False)),
]
