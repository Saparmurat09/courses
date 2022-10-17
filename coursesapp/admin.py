from django.contrib import admin
from .models import Contact, Category, Branch, Course
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    model = Branch

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    model = Course