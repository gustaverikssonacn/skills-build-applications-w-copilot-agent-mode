from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user=steve, activity_type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user=bruce, activity_type='swim', duration=25, date='2024-01-03')
        Activity.objects.create(user=clark, activity_type='yoga', duration=60, date='2024-01-04')

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 3 sets of 15 pushups', suggested_for='marvel')
        Workout.objects.create(name='Pullups', description='Do 3 sets of 10 pullups', suggested_for='dc')

        # Leaderboard
        Leaderboard.objects.create(user=tony, points=120)
        Leaderboard.objects.create(user=steve, points=110)
        Leaderboard.objects.create(user=bruce, points=130)
        Leaderboard.objects.create(user=clark, points=140)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
