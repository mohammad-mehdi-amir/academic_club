
from .models import User ,Profile


from django.test import TestCase
class Usertest(TestCase):

    def test_user_creation_default_role(self):
       
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.assertEqual(user.role, 'user')
        self.assertFalse(user.is_staff)

    def test_user_creation_member_role(self):
        
        member = User.objects.create_user(
            username='memberuser',
            password='testpass123',
            role='member'
        )
        self.assertEqual(member.role, 'member')
        self.assertTrue(member.is_staff)

    def test_user_creation_admin_role(self):
      
        admin = User.objects.create_user(
            username='adminuser',
            password='testpass123',
            role='admin'
        )
        self.assertEqual(admin.role, 'admin')
        self.assertFalse(admin.is_staff)  
        self.ass