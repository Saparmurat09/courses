from django.test import TestCase
from coursesapp.models import Category, Contact, Branch, Course

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
        cls.test_value = "+996550069420"

        Contact.objects.create(type_of=1, value=cls.test_value)


    def test_contact_value(self):
        contact = Contact.objects.get(id=1)

        self.assertEqual(contact.value, self.test_value)
    
    def test_contact_value_maxlenght(self):
        contact = Contact.objects.get(id=1)

        max_length = contact._meta.get_field('value').max_length

        self.assertEqual(100, max_length)

    
class TestBranch(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_latitude = "9820940282"
        cls.test_longitude = "1928379812"
        cls.test_address = "Usonbay, 59"

        Branch.objects.create(latitude=cls.test_latitude, longitude=cls.test_longitude, address=cls.test_address)

    def test_branch_latitude(self):
        branch = Branch.objects.get(id=1)

        self.assertEqual(branch.latitude, self.test_latitude)

    def test_branch_longitude(self):
        branch = Branch.objects.get(id=1)

        self.assertEqual(branch.longitude, self.test_longitude)
    
    def test_branch_address(self):
        branch = Branch.objects.get(id=1)

        self.assertEqual(branch.address, self.test_address)
    

class TestCourse(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_branch = Branch.objects.create(latitude="9820940282", longitude="1928379812", address="Usonbay, 59")
        cls.test_contact = Contact.objects.create(type_of=1, value="+996550069420")
        cls.test_category = Category.objects.create(name="Linear Algebra", imgpath="twitter.com/img/elon_musk")

        cls.test_name = "Mathematics with Prof. Jordan Peterson"
        cls.test_description = "Comprehensive Mathematics course"
        
        Course.objects.create(
            name=cls.test_name,
            description=cls.test_description,
            category=cls.test_category,
            logo="some logo",
            contacts=cls.test_contact,
            branches=cls.test_branch
        )

    def test_course_main_info(self):
        course = Course.objects.get(id=1)

        self.assertEqual(course.name, self.test_name)
        self.assertEqual(course.description, self.test_description)
    
    def test_course_category(self):
        course = Course.objects.get(id=1)

        self.assertEqual(course.category, self.test_category)
    
    def test_course_contact(self):
        course = Course.objects.get(id=1)

        self.assertEqual(course.contacts, self.test_contact)
    
    def test_course_branch(self):
        course = Course.objects.get(id=1)

        self.assertEqual(course.branches, self.test_branch)
    
    def test_course_multiple_branches(self):
        pass

