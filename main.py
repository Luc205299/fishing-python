import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
#FOR USING A GMAIL EMAIL FOLLOW THIS FOR THE CONNEXION : https://support.google.com/accounts/answer/185833?hl=en


def create_phishing_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = 'lecrackdephilo@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    return msg

def send_email(email_message,sender_email,password):
    smtp_server = 'smtp.gmail.com'
    port = 465  # Pour SSL
    sender_email = sender_email
    password = password

    # Créer une connexion SSL sécurisée
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(email_message['From'], email_message['To'], email_message.as_string())
            print("Email envoyé avec succès!")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        
def generate_tracking_link():
    base_url = "http://yourtrackingdomain.com/track?user="
    unique_id = "some_unique_identifier"  # Génère un ID unique pour chaque destinataire
    return base_url + unique_id
        
def main():
    
    print('|',end='')
    from_email = str(input("Insert your email : "))
    print('|',end='')
    password = str(input('Enter your email password : '))
    print('|',end='')
    to_email = str(input("Insert the email of the victim : "))
    print('|',end='')
    subject = str(input("Insert the subject : "))
    print('|',end='')
    user = str(input('Insert the Name of the victim'))
    print('|',end='')
    choice = int(input("Do you want a template email (1) or you want to write it by yourself (2) ?"))
    tracking_link = generate_tracking_link()
    body = f"""
    <html>
    <body>
        <p>Dear {user},</p>
        <p>There has been unusual activity on your account. Please <a href="{tracking_link}">click here</a> to verify your account information.</p>
        <p>Thank you,<br>Your Company</p>
    </body>
    </html>
    """
    email_message = create_phishing_email(to_email, subject, body)
    send_email(email_message,from_email,password)

if __name__ == "__main__":
    print(
        "|=========================================================================|\n"
        "|                    ,--.       ,--.                                      |\n"
        "|         ,-.----.     ,---,   ,--/  /|   ,--/  /|   ,---,                |\n"
        "|         \    /  \ ,`--.' |,---,': / ',---,': / '  '  .' \               |\n"
        "|         ;   :    \|   :  ::   : '/ / :   : '/ /  /  ;    '.             |\n"
        "|         |   | .\ ::   |  '|   '   ,  |   '   ,  :  :       \            |\n"
        "|         .   : |: ||   :  |'   |  /   '   |  /   :  |   /\   \           |\n"
        "|         |   |  \ :'   '  ;|   ;  ;   |   ;  ;   |  :  ' ;.   :          |\n"
        "|         |   : .  /|   |  |:   '   \  :   '   \  |  |  ;/  \   \         |\n" 
        "|         ;   | |  \'   :  ;|   |    ' |   |    ' '  :  | \  \ ,'          |\n"
        "|         |   | ;\  \   |  ''   : |.  \'   : |.  \|  |  '  '--'            |\n"
        "|         :   ' | \.'   :  ||   | '_\.'|   | '_\.'|  :  :                 |\n"
        "|         :   : :-' ;   |.' '   : |    '   : |    |  | ,'                 |\n"
        "|         |   |.'   '---'   ;   |,'    ;   |,'    `--''                   |\n"
        "|         `---'             '---'      '---'                              |\n"
        "|                                                                         |\n"
        "|=========================================================================|\n"
    )
    main()