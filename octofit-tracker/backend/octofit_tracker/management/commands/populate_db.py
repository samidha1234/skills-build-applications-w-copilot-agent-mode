
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample data
        marvel_team = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow'])
        dc_team = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman'])

        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Thor', email='thor@marvel.com', team='Marvel'),
            User(name='Hulk', email='hulk@marvel.com', team='Marvel'),
            User(name='Black Widow', email='widow@marvel.com', team='Marvel'),
            User(name='Superman', email='superman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Flash', email='flash@dc.com', team='DC'),
            User(name='Aquaman', email='aquaman@dc.com', team='DC'),
        ]
        User.objects.bulk_create(users)

        activities = [
            Activity(user='Iron Man', activity='Running', duration=30),
            Activity(user='Batman', activity='Cycling', duration=45),
            Activity(user='Wonder Woman', activity='Swimming', duration=60),
        ]
        Activity.objects.bulk_create(activities)

        leaderboard = [
            Leaderboard(team='Marvel', points=150),
            Leaderboard(team='DC', points=140),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        workouts = [
            Workout(user='Thor', workout='Strength', suggestion='Deadlift 5x5'),
            Workout(user='Flash', workout='Cardio', suggestion='Interval Sprints'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
