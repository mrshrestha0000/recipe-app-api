from typing_extensions import Self
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating new user with email successful"""

        email = 'success123shrestha@gmail.com'
        password = 'password'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_email_normalized(self):
        """Test the email for the new user is working"""

        email = 'success123shrestha@gmail.cOm'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """"Test creating user with no email"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')

    
    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser('success@gmail.com','password')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)