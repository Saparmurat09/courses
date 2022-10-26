from django.test import TestCase
from coursesapp.models import Category, Contact

class TestCategory(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_name = "Linear Algebra"
        cls.test_path = "twitter.com/img/elon_musk"
        Category.objects.create(name=cls.test_name, imgpath=cls.test_path)


    def test_category_name(self):
        category = Category.objects.get(id=1)

        self.assertEqual(category.name, self.test_name)

    def test_category_imgpath(self):
        category = Category.objects.get(id=1)
        
        self.assertEqual(category.imgpath, self.test_path)

    def test_category_object_name(self):
        category = Category.objects.get(id=1)

        self.assertEqual(str(category), self.test_name)

class TestContact(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_value = "+996069420"

        Contact.objects.create(type_of=1, value=cls.test_value)


    def test_contact_value(self):
        contact = Contact.objects.get(id=1)

        self.assertEqual(contact.value, self.test_value)
    
    def test_contact_value_maxlenght(self):
        contact = Contact.objects.get(id=1)

        max_length = contact._meta.get_field('value').max_length

        self.assertEqual(100, max_length)


        