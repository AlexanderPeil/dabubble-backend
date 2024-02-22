from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    reset_password_url = f"{settings.FRONTEND_URL}/reset-password?token={reset_password_token.key}"

    context = {
        'current_user': reset_password_token.user,
        'first_name': reset_password_token.user.first_name,
        'last_name': reset_password_token.user.last_name,
        'email': reset_password_token.user.email,
        'reset_password_url': reset_password_url
    }

    email_html_message = render_to_string('user_reset_password.html', context)
    email_plaintext_message = render_to_string('user_reset_password.txt', context)
         
    msg = EmailMultiAlternatives(
        "Password Reset for {title}".format(title="Password Reset for Videoflix"),
        email_plaintext_message,
        "Alcazar85@gmx.de",
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()