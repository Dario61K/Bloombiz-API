from django.conf import settings 

from django.core.mail import send_mail
from decouple import config as env

from typing import Dict, Any

from .emailConfigs import CUSTOM_EMAIL_CONFIGS
from .emailTemplates import (
    createAccountHTML,
    createAcount,
    resetPasswordHTML,
    resetPassword,
    changeEmailHTML,
    changeEmail
)

class EmailNotification():


    def create_account_notification(self, to, token):

        email_config: Dict[str:Any] = CUSTOM_EMAIL_CONFIGS.get('email_service_1') # type: ignore

        settings.EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
        settings.EMAIL_HOST = email_config['EMAIL_HOST']
        settings.EMAIL_PORT = email_config['EMAIL_PORT']
        
        send_mail(
            subject='Bloombiz Email Confirmation',
            html_message=createAccountHTML(token),
            message=createAcount(token),
            from_email=email_config['EMAIL_HOST_USER'],
            recipient_list=[to],
            auth_user=email_config['EMAIL_HOST_USER'],
            auth_password=email_config['EMAIL_HOST_PASSWORD'],
        )

    def reset_password_notification(self, to, token):
        
        email_config: Dict[str:Any] = CUSTOM_EMAIL_CONFIGS.get('email_service_1') # type: ignore

        settings.EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
        settings.EMAIL_HOST = email_config['EMAIL_HOST']
        settings.EMAIL_PORT = email_config['EMAIL_PORT']

        send_mail(
            subject='Bloombiz Email ',
            html_message=resetPasswordHTML(token),
            message=resetPassword(token),
            from_email=email_config['EMAIL_HOST_USER'],
            recipient_list=[to],
            auth_user=email_config['EMAIL_HOST_USER'],
            auth_password=email_config['EMAIL_HOST_PASSWORD'],
        )

    def change_email_notification(self, to, token):

        email_config: Dict[str:Any] = CUSTOM_EMAIL_CONFIGS.get('email_service_1') # type: ignore

        settings.EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
        settings.EMAIL_HOST = email_config['EMAIL_HOST']
        settings.EMAIL_PORT = email_config['EMAIL_PORT']

        send_mail(
            subject='Bloombiz Email ',
            html_message=changeEmailHTML(token),
            message=changeEmail(token),
            from_email=email_config['EMAIL_HOST_USER'],
            recipient_list=[to],
            auth_user=email_config['EMAIL_HOST_USER'],
            auth_password=email_config['EMAIL_HOST_PASSWORD'],
        )