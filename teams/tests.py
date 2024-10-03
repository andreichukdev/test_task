from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Team, Person


class PersonViewSetTests(APITestCase):

    def setUp(self):
        # Створюємо тестову команду і людину
        self.team = Team.objects.create(name="Team Alpha")
        self.person = Person.objects.create(
            first_name="Alex",
            last_name="Shevelo",
            email="alex.shevelo@gmail.com",
            team=self.team
        )

    def test_get_person_list(self):
        # Перевіряємо отримання списку людей
        url = reverse('person-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_person(self):
        # Перевіряємо створення нової людини
        url = reverse('person-list')
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "team": self.team.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)

    def test_retrieve_person(self):
        # Перевіряємо отримання детальної інформації про людину
        url = reverse('person-detail', kwargs={'pk': self.person.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], "Ivan")

    def test_update_person(self):
        # Перевіряємо оновлення людини
        url = reverse('person-detail', kwargs={'pk': self.person.id})
        data = {
            "first_name": "Updated Alex",
            "last_name": "Shevelo",
            "email": "alex.shevelo@gmail.com",
            "team": self.team.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.first_name, "Updated Alex")

    def test_delete_person(self):
        # Перевіряємо видалення людини
        url = reverse('person-detail', kwargs={'pk': self.person.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0) 


class TeamViewSetTests(APITestCase):

    def setUp(self):
        # Створюємо тестову команду
        self.team = Team.objects.create(name="Team Alpha")

    def test_get_team_list(self):
        # Перевіряємо отримання списку команд
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_team(self):
        # Перевіряємо створення нової команди
        url = reverse('team-list')
        data = {"name": "Team Beta"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)

    def test_retrieve_team(self):
        # Перевіряємо отримання детальної інформації про команду
        url = reverse('team-detail', kwargs={'pk': self.team.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Team Alpha")

    def test_update_team(self):
        # Перевіряємо оновлення команди
        url = reverse('team-detail', kwargs={'pk': self.team.id})
        data = {"name": "Updated Team Alpha"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, "Updated Team Alpha")

    def test_delete_team(self):
        # Перевіряємо видалення команди
        url = reverse('team-detail', kwargs={'pk': self.team.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 0)



