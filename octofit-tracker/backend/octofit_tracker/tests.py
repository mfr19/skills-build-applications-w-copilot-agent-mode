from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)
        self.workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Pushups')
