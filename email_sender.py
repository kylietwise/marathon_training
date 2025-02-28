import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, email_config):
        """
        Initializes the email sender with configuration settings.
        """
        self.smtp_server = email_config['smtp_server']
        self.smtp_port = email_config['smtp_port']
        self.from_email = email_config['from_email']
        self.to_email = email_config['to_email']
        self.email_password = email_config['email_password']

    def send_email(self, plan):
        """
        Sends the training plan via email.
        """
        subject = "Your Weekly Training Plan"
        body = "<h1>Your Weekly Training Plan</h1><ul>"
        for day, workout in plan.items():
            body += f"<li><strong>{day}:</strong> {workout}</li>"
        body += "</ul>"
        
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.email_password)
            server.sendmail(self.from_email, self.to_email, msg.as_string())
            server.quit()
            print(f"Email sent successfully to {self.to_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")