from django.test import TestCase
from .models import Vacancy


class HomepageTestCase(TestCase):
    def test_open_homepage_should_success(self):
        response = self.client.get('/')
        assert response.status_code == 200
        # response_1 = self.client.get('/workers')
        # assert response_1.status_code == 301
        # assert 'Поиск работы и работников' in response

    # def test_post_request_homepage_should_405(self):
    #     response = self.client.post('/')
    #     assert response.status_code == 405


class VacancyTestCase(TestCase):
    def test_create_vacancy_should_success(self):
        my_data = {
            "titlee": "test_1",
            "salary": "100",
            "email": "test_1@.com",
            "description": "test description 1"
        }

        response = self.client.post("/vacancies-add/", my_data)
        self.assertEqual(response.status_code, 200)

        new_vacancy = Vacancy.objects.first()
        self.assertEqual(new_vacancy.title, "test_1")
        self.assertEqual(new_vacancy.salary, int("100"))
        self.assertEqual(new_vacancy.email, "test_1@.com")
        self.assertEqual(new_vacancy.description, "test description 1")
