import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 587  

sender_email = "muhammadayansajid2005@gmail.com"
password = "cczx islp pmcq ejuo" 
receiver_email = "2024cs696@student.uet.edu.pk"

subject = "Test Email from Python"
body = """\
Hello!
This is a test email sent from Python using Gmail SMTP over TCP with TLS.
"""

message = f"Subject: {subject}\n\n{body}"

context = ssl.create_default_context()
 
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  
    server.starttls(context=context)  # Upgrade connection to secure TLS
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

print(" Email sent successfully!")