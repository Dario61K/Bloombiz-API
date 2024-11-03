from decouple import config as env


def createAccountHTML(token):
    url = f"{env('CONFIRMATION_ACCOUNT_LINK')}/{token}"

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Your Registration</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            overflow-x: hidden; /* Prevent horizontal scrolling */
        }}
        .container {{
            width: 100%; /* Ensure the container uses 100% width up to max-width */
            margin: auto; /* Center the container */
            padding: 50px 20px;
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            box-sizing: border-box; /* Include padding in width calculations */
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #7019fc;
            color: #ffffff !important; /* Ensure the text color stays white */
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }}
        .footer {{
            text-align: center;
            font-size: 12px;
            color: #888888;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="logo" style="text-align: center; margin-bottom: 20px;">
            <img src="https://ik.imagekit.io/xb3lv4fjl/Bloombiz/logo%20bloombiz.png?updatedAt=1730608559335" alt="Bloombiz Logo" width="80">
        </div>
        <h1 style="text-align: center;">Welcome to Bloombiz!</h1>
        <p style="text-align: center;">Click the button or link below to complete your registration and get started with Bloombiz.</p>
        <p style="text-align: center; margin: 20px 0;">
            <a href="{url}" class="button">Complete your registration</a>
        </p>
        <hr style="width: 70%; margin: 40px auto;">
        <div class="footer">
            <p>If you have problems with the button, copy and paste the following link into your browser:</p>
            <p style="word-break: break-word; text-align: center; max-width: 70%; margin: 0 auto;">
                <a href="{url}">{url}</a>
            </p>
        </div>
    </div>
</body>
</html>
    """

def createAcount(token):

    url = f"{env('CONFIRMATION_ACCOUNT_LINK')}/{token}"

    return f"""
        Welcome to Bloombiz!

        Click the link below to complete your registration and get started with Bloombiz:

        {url}    
    """


def resetPasswordHTML(token):

    url = f"{env('RESET_PASSWORD_LINK')}/{token}"

    return f"""

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Reset Request</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            overflow-x: hidden; /* Prevent horizontal scrolling */
        }}
        .container {{
            width: 100%; /* Ensure the container uses 100% width up to max-width */
            margin: auto; /* Center the container */
            padding: 50px 20px;
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            box-sizing: border-box; /* Include padding in width calculations */
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #7019fc;
            color: #ffffff !important; /* Ensure the text color stays white */
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }}
        .footer {{
            text-align: center;
            font-size: 12px;
            color: #888888;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="logo" style="text-align: center; margin-bottom: 20px;">
            <img src="https://ik.imagekit.io/xb3lv4fjl/Bloombiz/logo%20bloombiz.png?updatedAt=1730608559335" alt="Bloombiz Logo" width="80">
        </div>
        <h1 style="text-align: center;">Password Reset Request</h1>
        <p style="text-align: center;">To reset your password, please click the button or the link below.</p>
        <p style="text-align: center; margin: 20px 0;">
            <a href="{url}" class="button">Reset Your Password</a>
        </p>
        <hr style="width: 70%; margin: 40px auto;">
        <div class="footer">
            <p>If you encounter any issues with the button, copy and paste the following link into your browser:</p>
            <p style="word-break: break-word; text-align: center; max-width: 70%; margin: 0 auto;">
                <a href="{url}">{url}e</a>
            </p>
        </div>
    </div>
</body>
</html>
"""

def resetPassword(token):

    url = f"{env('RESET_PASSWORD_LINK')}/{token}"

    return f"""
        Password Reset Request

        To reset your password, please click the link below

        {url}    
    """

def changeEmailHTML(token):

    url = f"{env('CHANGE_EMAIL_LINK')}/{token}"

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Change Request</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            overflow-x: hidden; /* Prevent horizontal scrolling */
        }}
        .container {{
            width: 100%; /* Ensure the container uses 100% width up to max-width */
            margin: auto; /* Center the container */
            padding: 50px 20px;
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            box-sizing: border-box; /* Include padding in width calculations */
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            background-color: #7019fc;
            color: #ffffff !important; /* Ensure the text color stays white */
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }}
        .footer {{
            text-align: center;
            font-size: 12px;
            color: #888888;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="logo" style="text-align: center; margin-bottom: 20px;">
            <img src="https://ik.imagekit.io/xb3lv4fjl/Bloombiz/logo%20bloombiz.png?updatedAt=1730608559335" alt="Bloombiz Logo" width="80">
        </div>
        <h1 style="text-align: center;">Email Change Request</h1>
        <p style="text-align: center;">To confirm your new email address, please click the button or the link below.</p>
        <p style="text-align: center; margin: 20px 0;">
            <a href="{url}" class="button">Confirm Your New Email</a>
        </p>
        <hr style="width: 70%; margin: 40px auto;">
        <div class="footer">
            <p>If you encounter any issues with the button, copy and paste the following link into your browser:</p>
            <p style="word-break: break-word; text-align: center; max-width: 70%; margin: 0 auto;">
                <a href="{url}">{url}</a>
            </p>
        </div>
    </div>
</body>
</html>

"""

def changeEmail(token):

    url = f"{env('CHANGE_EMAIL_LINK')}/{token}"

    return f"""
        Email Change Request

        To confirm your new email address, please click the link below

        {url}    
    """