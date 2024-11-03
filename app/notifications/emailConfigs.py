from decouple import config as env


CUSTOM_EMAIL_CONFIGS = {
        'email_service_1': {
            'EMAIL_HOST_USER': env('EMAIL_HOST_USER_1'),
            'EMAIL_HOST_PASSWORD': env('EMAIL_PASSWORD_1'),
            'EMAIL_HOST': env('EMAIL_HOST_1'),
            'EMAIL_PORT': env('EMAIL_PORT_1'),
            'EMAIL_USE_TLS': env('EMAIL_USE_TLS_1'),
        }
    }