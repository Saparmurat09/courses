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
    
    def create(self, validated_data):
        branches_data = validated_data.pop('branches')
        category_data = validated_data.pop('category')
        contacts_data = validated_data.pop('contacts')

        course = Course.objects.create(**validated_data)

        course.branches = Branch.objects.create(**branches_data)
        course.category = Category.objects.create(**category_data)
        course.contacts = Contact.objects.create(**contacts_data)

        course.save()

        return course