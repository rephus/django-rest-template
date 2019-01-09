from django.test import TestCase
from rest_framework.test import APITestCase
from todo.factories import TaskFactory
from todo.models import Task

class TaskTest(APITestCase):

    def test_create(self):
        task = TaskFactory()
        inserted = Task.objects.create(title=task.title)
        self.assertEqual(inserted.title, task.title)
        self.assertNotEqual(inserted.id, task.id )

    def test_get(self):
        task = TaskFactory()
        inserted = Task.objects.get(id=task.id)
        self.assertEqual(inserted.title, task.title)
