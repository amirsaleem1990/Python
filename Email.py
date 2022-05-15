#!/usr/bin/python3
def Email(subject, mail_to, mail_from, mail_pass, body, body_2=""):
    """
    Usage: Email(subject, mail_to, mail_from, mail_pass, body, body_2="")
    
    """
    import smtplib, ssl
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = mail_pass
    message = f"""\
    Subject: {subject}

    {body}

    
    {body_2}
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(mail_from, password)
        server.sendmail(mail_from, mail_to, message)

