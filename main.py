from training_plan import TrainingPlan
from email_sender import EmailSender
from email_scheduler import EmailScheduler
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TrainingPlanEmailAutomation:
    def __init__(self, email_config, schedule_config):
        """
        Initializes the automation system by setting up email and schedule configs.
        """
        self.email_config = email_config
        self.schedule_config = schedule_config

        # Initialize instances for the classes
        self.plan_generator = TrainingPlan()
        self.email_sender = EmailSender(email_config)
        self.scheduler = EmailScheduler(self.email_sender, schedule_config)

    def run(self):
        """
        Main function to generate a training plan and send out weekly email.
        """
        try:
            # Generate the training plan
            logger.info("Generating the training plan...")
            plan = self.plan_generator.generate()

            # Send the training plan via email
            logger.info("Sending the training plan email...")
            self.email_sender.send_email(plan)

            # Schedule weekly email dispatch
            logger.info("Scheduling weekly email sending...")
            self.scheduler.schedule_emails()

        except Exception as e:
            logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example configuration data
    email_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'from_email': 'your_email@example.com',
        'to_email': 'recipient@example.com',
        'email_password': 'your_email_password'
    }

    schedule_config = {
        'send_time': '08:00',  # Set the time you want emails to be sent every week
        'day_of_week': 'monday'
    }

    automation = TrainingPlanEmailAutomation(email_config, schedule_config)
    automation.run()
