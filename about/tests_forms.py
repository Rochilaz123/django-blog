from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'tester',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), 
        msg="Form is not valid")

    def test_name_is_required(self):
        """Test for 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), 
        msg="Name was not provided but form is valid")

    def test_email_not_valid(self):
        """Test for email field"""
        form = CollaborateForm({
            'name': 'Myself',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), 
        msg="Email was not provided but form is valid")


    def test_message_not_valid(self):
        """Test for message field"""
        form = CollaborateForm({
            'name': 'Myself',
            'email': 'test@email.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(),
        msg="Message was not provided but form is valid")