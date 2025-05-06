import threading
from django.core.mail import send_mail
from django.conf import settings




def send_email(subject, message, to_email):
    send_mail(subject=subject,
              message=message,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[to_email],
              fail_silently=True
    )





def send_email_thread(subject,message,to_email):
    thread = threading.Thread(target=send_email, args=(subject,message,to_email))
    thread.start()



