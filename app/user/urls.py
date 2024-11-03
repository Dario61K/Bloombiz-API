from django.urls import path
from .views import (
    CreateAccountRequest,
    CreateAccountConfirm,
    ResetPasswordRequest,
    ResetPasswordVerify,
    ResetPasswordChange,
    ChangeName,
    ChangePassword,
    ChangeEmailRequest,
    ChangeEmailConfirm,
    DeleteAccount
)

urlpatterns = [
    path('create_account/request/', CreateAccountRequest.as_view(), name='create_account_request'),
    path('create_account/confirm/<str:token>', CreateAccountConfirm.as_view(), name='create_account_confirm'),

    path('reset_password/request/', ResetPasswordRequest.as_view(), name='reset_password_request'),
    path('reset_password/verify/<str:token>', ResetPasswordVerify.as_view(), name='reset_password_verify'),
    path('reset_password/change/<str:token>', ResetPasswordChange.as_view(), name='reset_password_change'),

    path('change_name/', ChangeName.as_view(), name='change_name'),  # login required
    path('change_password/', ChangePassword.as_view(), name='change_password'),  # login required
    path('change_email/request', ChangeEmailRequest.as_view(), name='change_email_request'),  # login required
    path('change_email/confirm/<str:token>', ChangeEmailConfirm.as_view(), name='change_email_confirm'),  # login required

    path('delete_account', DeleteAccount.as_view(), name='delete_account') # login required
]
