from django.test import TestCase, Client


class TestCreateBook(TestCase):
    def test_create_book(self):
        a = Client()
        response = a.get('http://127.0.0.1:8000/book/', data={
            "name": 'asdasfsad',
            "price": '12345',
            "description": 'jksdncsd',
            "image": '',
            "type": '',
        })
        assert response.status_code == 200




# class TestHomepage(TestCase):
#     def test_open_homepage_should_be_success(self):
#         c = Client()
#         response = c.get('http://127.0.0.1:8000/')
#         assert "Hello world" in str(response.content)
#         assert response.status_code == 200
#
#     def test_post_homepage_should_return_405(self):
#         c = Client()
#         response = c.post('http://127.0.0.1:8000/')
#         assert response.status_code == 405, f'{response.status_code} should be 405'
#
#
# class TestProductCreate(TestCase):
#     def test_should_allow_only_post(self):
#         c = Client()
#         response = c.get('http://127.0.0.1:8000/product/')
#         assert response.status_code == 405
#         response = c.put('http://127.0.0.1:8000/product/')
#         assert response.status_code == 405
#         response = c.patch('http://127.0.0.1:8000/product/')
#         assert response.status_code == 405
#         response = c.delete('http://127.0.0.1:8000/product/')
#         assert response.status_code == 405
#
#     def should_create_object(self):
#         c = Client()
#         response = c.post('http://127.0.0.1:8000/product/', data={
#             "name": 'Hello',
#             "price": 200
#         }
#                           )
#         assert response.status_code == 201
