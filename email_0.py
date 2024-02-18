import smtplib

# Email configuration
# sender_email = "amir.saleem@lovefordata.com"
sender_email = "amir.kids.vids@gmail.com"
receiver_email = "amir.saleem@lovefordata.com"
# password = "tradersLFDgmail1990"
password = "2sm7fZtMaHQtSZ7"

# Message configuration
subject = "Subject Line"
body = "Email body text"
message = f'Subject: {subject}\n\n{body}'

# Sending email
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, receiver_email, message)


# import sys
# import sqlalchemy
# import smtplib
# import pandas as pd
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from fpdf import FPDF

# MAIL_FROM = "amir.saleem@lovefordata.com"
# MAIL_HOST = "smtp.gmail.com"
# MAIL_PORT = 587
# MAIL_PASS = "tradersLFDgmail1990"


# def send_email(MAIL_TO, body, subject):
# 	print(f"Sending Email to {MAIL_TO} ................ ")
# 	s = smtplib.SMTP(f'{MAIL_HOST}:{MAIL_PORT}')
# 	s.starttls()
# 	s.login(MAIL_FROM, MAIL_PASS)

# 	msg = MIMEMultipart()
# 	msg['Subject'] = subject
# 	msg['From'] = MAIL_FROM
# 	msg['To'] = MAIL_TO
# 	# msg['Cc'] = "noman@lovefordata.com,maira@lovefordata.com,syed@lovefordata.com"

# 	txt = MIMEText(body)
# 	msg.attach(txt)

# 	s.send_message(msg)
# 	s.quit()
# send_email(MAIL_TO='amir.saleem@lovefordata.com', body="body", subject="subject")