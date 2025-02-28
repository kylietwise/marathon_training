from training_plan import TrainingPlan

import datetime

class TrainingPlan:
    def __init__(self):
        """
        Initializes the training plan generator.
        """
        self.plan = {}

    def generate(self):
        """
        Generates a simple weekly workout plan.
        """
        today = datetime.date.today()
        week_start = today - datetime.timedelta(days=today.weekday())  # Start of the week (Monday)
        
        self.plan = {
            "Monday": "Cardio: 30 min run",
            "Tuesday": "Strength: Full body workout",
            "Wednesday": "Rest or Yoga",
            "Thursday": "Cardio: 45 min cycling",
            "Friday": "Strength: Upper body workout",
            "Saturday": "Rest or Outdoor activity",
            "Sunday": "Stretch and recovery"
        }
        return self.plan