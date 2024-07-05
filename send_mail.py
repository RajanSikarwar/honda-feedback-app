import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'bccfea76068bf6'
    password = '62323766a73d33'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    
    sender_email = "email@sender.com"
    reciever_email = "email@reciever.com"
    msg = MIMEText(message , 'html')
    msg['Subject'] = "Honda Feedback"
    msg['From'] = sender_email
    msg['To'] = reciever_email

    #Send the mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())