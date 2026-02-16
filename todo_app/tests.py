from django.test import TestCase
from .models import Task,Author
from django.utils import timezone

# Create your tests here.
class TaskMOdelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Edward Tester")
        email = 'mbatha@gmail.com'
    def test_task_str(self):
        task = Task(
            title = "Write Tests",
            description = "Ensuring all nodels attributes have correct tests",
            due_date = timezone.now().date(),
            author = self.author
        )

        expected_str = "Title: Write Tests\n description:Ensuring all nodels attributes have correct tests"
            

        

        self.assertEqual(str(task), expected_str)
