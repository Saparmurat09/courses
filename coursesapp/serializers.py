from .models import Course, Contact, Category, Branch

from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type_of', 'value']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'imgpath']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer()
    category = CategorySerializer()
    contacts = ContactSerializer()
    class Meta:
        model = Course
        fields = ['name', 'description', 'category', 'logo', 'contacts', 'branches']
