from django.test import TestCase

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import *


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "first todo app",
            body = "this has been a great memory",
        )


    def test_model_content(self):
        self.assertEqual(self.todo.title, "first todo app")
        self.assertEqual(self.todo.body, "this has been a great memory")
        self.assertEqual(str(self.todo), "first todo app")


    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "first todo app")