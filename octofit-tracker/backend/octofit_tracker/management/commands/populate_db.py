
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('populate_db command started')
        User = get_user_model()
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        try:
            # Create teams
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')
            self.stdout.write(f"Created teams: {marvel.name} (id={marvel.pk}), {dc.name} (id={dc.pk})")

            # Create users
            ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
            cap = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password')
            batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
            superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')
            self.stdout.write(f"Created users: {ironman.username} (id={ironman.pk}), {cap.username} (id={cap.pk}), {batman.username} (id={batman.pk}), {superman.username} (id={superman.pk})")

            # Create activities (ForeignKey to User)
            a1 = Activity.objects.create(user=ironman, activity_type='Running', duration=30)
            a2 = Activity.objects.create(user=batman, activity_type='Cycling', duration=45)
            self.stdout.write(f"Created activities: {a1.activity_type} for {a1.user.username} (id={a1.pk}), {a2.activity_type} for {a2.user.username} (id={a2.pk})")

            # Create leaderboard (ForeignKey to User)
            l1 = Leaderboard.objects.create(user=ironman, points=100)
            l2 = Leaderboard.objects.create(user=batman, points=120)
            self.stdout.write(f"Created leaderboard entries: {l1.user.username} ({l1.points} pts, id={l1.pk}), {l2.user.username} ({l2.points} pts, id={l2.pk})")

            # Create workouts
            w1 = Workout.objects.create(name='Morning Cardio', description='A quick morning cardio session.')
            w2 = Workout.objects.create(name='Strength Training', description='Full body strength workout.')
            self.stdout.write(f"Created workouts: {w1.name} (id={w1.pk}), {w2.name} (id={w2.pk})")

            self.stdout.write(self.style.SUCCESS('Database populated with sample data.'))
        except Exception as e:
            import traceback
            tb = traceback.format_exc()
            self.stdout.write(self.style.ERROR(f'Error during population: {e}'))
            self.stdout.write(self.style.ERROR(tb))
            self.stdout.write(self.style.ERROR(f'Error populating database: {e}'))

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
