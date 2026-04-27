
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('populate_db command started')
        User = get_user_model()
        
        try:
            # Clear existing data - simpler approach
            self.stdout.write('Clearing existing data...')
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()
            
            self.stdout.write('Creating teams...')
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')
            self.stdout.write(f"Created teams: {marvel.name}, {dc.name}")

            self.stdout.write('Creating users...')
            ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
            cap = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password')
            batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
            superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')
            self.stdout.write(f"Created users: {ironman.username}, {cap.username}, {batman.username}, {superman.username}")

            self.stdout.write('Creating activities...')
            a1 = Activity.objects.create(user_id=str(ironman.id), user_name=ironman.username, activity_type='Running', duration=30)
            a2 = Activity.objects.create(user_id=str(batman.id), user_name=batman.username, activity_type='Cycling', duration=45)
            a3 = Activity.objects.create(user_id=str(cap.id), user_name=cap.username, activity_type='Swimming', duration=60)
            a4 = Activity.objects.create(user_id=str(superman.id), user_name=superman.username, activity_type='Weightlifting', duration=90)
            self.stdout.write(f"Created 4 activities")

            self.stdout.write('Creating leaderboard entries...')
            l1 = Leaderboard.objects.create(user_id=str(ironman.id), user_name=ironman.username, points=100)
            l2 = Leaderboard.objects.create(user_id=str(batman.id), user_name=batman.username, points=120)
            l3 = Leaderboard.objects.create(user_id=str(superman.id), user_name=superman.username, points=150)
            l4 = Leaderboard.objects.create(user_id=str(cap.id), user_name=cap.username, points=110)
            self.stdout.write(f"Created 4 leaderboard entries")

            self.stdout.write('Creating workouts...')
            w1 = Workout.objects.create(name='Morning Cardio', description='A quick morning cardio session.')
            w2 = Workout.objects.create(name='Strength Training', description='Full body strength workout.')
            w3 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
            w4 = Workout.objects.create(name='Situps', description='Do 30 situps')
            self.stdout.write(f"Created 4 workouts")

            self.stdout.write(self.style.SUCCESS('Database populated with sample data.'))
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            self.stdout.write(self.style.ERROR(f'Error during population: {e}'))
            self.stdout.write(self.style.ERROR(tb))

