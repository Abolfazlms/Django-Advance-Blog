from django.test import TestCase
from datetime import datetime
from ..forms import PostForms
from ..models import Category
class TestPostForm(TestCase):
    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name='hello')
        form = PostForms(data={
            "title":"test",
            "content":"test description",
            "status":True,
            "category":category_obj,
            "published_date":datetime.now()})
        self.assertTrue(form.is_valid())
    def test_post_form_with_no_data(self):
        form = PostForms(data={})
        self.assertFalse(form.is_valid())
        