from django.test import TestCase
from rest_framework.test import APITestCase
from todo.factories import TaskFactory
from todo.models import Task

class StatusTest(APITestCase): 
    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(result['name'], 'todo')

    def test_ping(self):
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'pong')


class TaskViewSetTest(APITestCase):

    def test_post_task(self):
        task = TaskFactory()
        task_json =  {
            "title": task.title,
        } 
        response = self.client.post('/task', task_json, format='json')

        self.assertEqual(response.status_code, 201)
        result = response.json()

        self.assertEqual(result['title'], task.title)
        self.assertEqual(result['completed'], False) # default
        self.assertEqual(result['description'], None) # default

    def test_get_all_tasks(self):
        task = TaskFactory()

        response = self.client.get('/task')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        self.assertEqual(result['count'], 1)
        inserted_task = result['results'][0]
        self.assertEqual(inserted_task['id'], str(task.id))
        self.assertEqual(inserted_task['title'], task.title)

    def test_delete_task(self):
        TaskFactory()

        self.assertEqual(Task.objects.count(), 1) 
        task = Task.objects.first()
        response = self.client.delete('/task/{}'.format(str(task.id)))
        self.assertEqual(response.status_code, 204)
        
        self.assertEqual(Task.objects.count(), 0) 
