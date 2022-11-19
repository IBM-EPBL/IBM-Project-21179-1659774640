import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('FFS0xxbiT4SCeWBhld-M5w.D9m23Sg7KHUBZMdpsS6iU5kyNFckz-munEctuuUokSo'))
from_email = Email("19cs080@kcgcollege.com")  # Change to your verified sender
to_email = To("19cs082@kcgcollege.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)
