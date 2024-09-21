from django.test import TestCase
from datetime import datetime
# from django.contrib.auth import get_user_model
from ..models import Post
from accounts.models import User, Profile
class TestPostModel(TestCase):
    def test_create_post_with_valid_data(self):
        user = User.objects.create_user(email='test@test.com',password='12345678@')
        profile = Profile.objects.create(
            user=user,
            first_name='test_name',
            last_name='test_last_name',
            description='test description about test user',
            )
        post = Post.objects.create(
            author = profile,
            title = "test",
            content = "test description",
            status = True,
            category =None,
            published_date = datetime.now(),
        )
        self.assertEquals(post.title,'test')