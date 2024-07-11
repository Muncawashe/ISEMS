from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Department, Role, User, Session, Leave, Task, Message
from datetime import datetime, timedelta

User = get_user_model()

class DepartmentModelTest(TestCase):
    def setUp(self):
        Department.objects.create(name="Engineering")

    def test_department_creation(self):
        dept = Department.objects.get(name="Engineering")
        self.assertEqual(dept.name, "Engineering")

class RoleModelTest(TestCase):
    def setUp(self):
        Role.objects.create(name="Manager")

    def test_role_creation(self):
        role = Role.objects.get(name="Manager")
        self.assertEqual(role.name, "Manager")

class UserModelTest(TestCase):
    def setUp(self):
        dept = Department.objects.create(name="Engineering")
        role = Role.objects.create(name="Manager")
        User.objects.create_user(username="john_doe", password="password123", phone=1234567890, dept=dept, role=role)

    def test_user_creation(self):
        user = User.objects.get(username="john_doe")
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.phone, 1234567890)
        self.assertEqual(user.dept.name, "Engineering")
        self.assertEqual(user.role.name, "Manager")

class SessionModelTest(TestCase):
    def setUp(self):
        dept = Department.objects.create(name="Engineering")
        role = Role.objects.create(name="Manager")
        user = User.objects.create_user(username="john_doe", password="password123", phone=1234567890, dept=dept, role=role)
        Session.objects.create(user=user, login_time=datetime.now(), logout_time=datetime.now() + timedelta(hours=1))

    def test_session_creation(self):
        session = Session.objects.get(user__username="john_doe")
        self.assertEqual(session.user.username, "john_doe")
        self.assertIsNotNone(session.login_time)
        self.assertIsNotNone(session.logout_time)

class LeaveModelTest(TestCase):
    def setUp(self):
        dept = Department.objects.create(name="Engineering")
        role = Role.objects.create(name="Manager")
        user = User.objects.create_user(username="john_doe", password="password123", phone=1234567890, dept=dept, role=role)
        Leave.objects.create(user=user, start="2024-01-01", end="2024-01-10", reason="Vacation", approved=True)

    def test_leave_creation(self):
        leave = Leave.objects.get(user__username="john_doe")
        self.assertEqual(leave.user.username, "john_doe")
        self.assertEqual(leave.reason, "Vacation")
        self.assertTrue(leave.approved)

class TaskModelTest(TestCase):
    def setUp(self):
        dept = Department.objects.create(name="Engineering")
        role = Role.objects.create(name="Manager")
        user = User.objects.create_user(username="john_doe", password="password123", phone=1234567890, dept=dept, role=role)
        Task.objects.create(title="Task 1", description="Task 1 description", end="2024-12-31", assigned_to=user, approved=True, perfomance=80)

    def test_task_creation(self):
        task = Task.objects.get(title="Task 1")
        self.assertEqual(task.title, "Task 1")
        self.assertEqual(task.description, "Task 1 description")
        self.assertEqual(task.assigned_to.username, "john_doe")
        self.assertTrue(task.approved)
        self.assertEqual(task.perfomance, 80)

class MessageModelTest(TestCase):
    def setUp(self):
        dept = Department.objects.create(name="Engineering")
        role = Role.objects.create(name="Manager")
        user = User.objects.create_user(username="john_doe", password="password123", phone=1234567890, dept=dept, role=role)
        Message.objects.create(msg="Hello, John!", sent_to=user)

    def test_message_creation(self):
        message = Message.objects.get(sent_to__username="john_doe")
        self.assertEqual(message.msg, "Hello, John!")
        self.assertEqual(message.sent_to.username, "john_doe")

