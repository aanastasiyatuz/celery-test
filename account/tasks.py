from celery import shared_task

@shared_task
def send_activation_code(activation_code, email):
    from django.core.mail import send_mail
    activation_link = f'http://127.0.0.1:8000/account/activate/{activation_code}'
    message = f'Активируйте свой аккаунт, перейдя по ссылке:\n{activation_link}'
    send_mail("Activate account", message, 'aanastasiyatuz@gmail.com', [email])
