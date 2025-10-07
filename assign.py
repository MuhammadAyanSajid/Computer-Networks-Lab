import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 587  

sender_email = "muhammadayansajid2005@gmail.com"
password = "cczx islp pmcq ejuo" 
receiver_email = "2024cs661@student.uet.edu.pk"

subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")
 
message = f"Subject: {subject}\n\n{body}"

context = ssl.create_default_context()
 
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  
    server.starttls(context=context)  
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

print(" Email sent successfully!")