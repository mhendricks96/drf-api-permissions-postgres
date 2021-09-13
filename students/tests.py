from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Student

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_student = Student.objects.create(
            admitted_by = testuser1,
            name = 'Jane Doe',
            major = 'science',
            graduation_date = '2022-08-09',
            birth_date = '1987-12-03'
        )
        test_student.save()

    def test_student_content(self):
        student = Student.objects.get(id=1)
        actual_administator = str(student.admitted_by)
        actual_name = str(student.name)
        actual_major = str(student.major)
        self.assertEqual(actual_administator, 'testuser1')
        self.assertEqual(actual_name, 'Jane Doe')
        self.assertEqual(actual_major, 'science')

# Create your tests here.
