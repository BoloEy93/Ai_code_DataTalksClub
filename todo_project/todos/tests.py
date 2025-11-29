from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(title="Test Todo", due_date="2023-12-31", resolved=False)

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.due_date.strftime("%Y-%m-%d"), "2023-12-31")
        self.assertFalse(self.todo.resolved)

    def test_todo_mark_as_resolved(self):
        self.todo.resolved = True
        self.todo.save()
        self.assertTrue(self.todo.resolved)

    def test_todo_string_representation(self):
        self.assertEqual(str(self.todo), "Test Todo")