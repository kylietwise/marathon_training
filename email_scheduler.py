import schedule
import time

class EmailScheduler:
    def __init__(self, email_sender, schedule_config):
        """
        Initializes the email scheduler with the email sender and schedule configuration.
        """
        self.email_sender = email_sender
        self.schedule_config = schedule_config

    def send_scheduled_email(self):
        """
        Function to send the scheduled email.
        """
        plan = self.email_sender.plan  # Get the plan from the email sender
        self.email_sender.send_email(plan)

    def schedule_emails(self):
        """
        Schedules the emails based on the user's preferred schedule.
        """
        day_of_week = self.schedule_config['day_of_week']
        send_time = self.schedule_config['send_time']

        # Scheduling logic
        schedule.every().monday.at(send_time).do(self.send_scheduled_email)  # Can be changed based on the config

        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute for the scheduled task
