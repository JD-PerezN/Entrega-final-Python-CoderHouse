from django.test import TestCase
from django.urls import reverse, reverse_lazy

from AppBlog import models


## Create your tests here.
# Test for index page
class URLTest(TestCase):
    def test_url_inicio(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get(reverse('appblog-inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AppBlog/post-list-index.html')

    def test_url_register(self):
        response = self.client.get("/crear-usuario/")
        self.assertEqual(response.status_code, 200)

# Test for 
class PostListViewTest(TestCase):
    def set_up_test_data(cls):
        models.Post.objects.create(title="post_test",
                                   slug="slug_test",
                                   author="author_test",
                                   content="content_test",
                                   status=1)
        
    def setUpTestData(cls):
        number_post = 20
        for post_id in range(number_post):
            models.Post.objects.create(title=f"title_{post_id}",
                                       slug=f"slug_{post_id}",
                                       author=f"author_{post_id}",
                                       content=f"content_{post_id}",
                                       status=1)
        
    
    
            