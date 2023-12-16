import smtplib
import csv

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# my_address = 'vantheldriel@gmail.com'
# password = 'app_password'

my_address = 'sender_email@gmail.com'
password = 'app_password'
message_title = 'Message title.'

def get_contacts(filename):

    # Return email addresses read from a file specified by filename.
    emails = []
    with open(filename, newline='') as contacts_file:
        emailreader = csv.reader(contacts_file, delimiter=' ', quotechar='|')
        for a_contact in emailreader:
            emails.append(a_contact)

    formatted_emails = [e[:][0] for e in emails]
    return formatted_emails


def main():

    # Read contacts from a CSV file named 'all_emails.csv'
    formatted_emails = get_contacts('email_list_part9.csv')
    message ="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi porta diam in nulla fringilla, vitae sollicitudin
justo rhoncus. Cras tincidunt ante dui, ac auctor ante fermentum quis. Aliquam bibendum semper lacus quis faucibus.
Proin porttitor nibh urna, vitae semper purus bibendum sodales. Aliquam eu pulvinar dui, ac egestas quam. Morbi
venenatis lacus id laoreet dignissim. Nam eu sapien nunc. Mauris aliquet, lacus ut consectetur vulputate, orci dui
euismod dolor, mollis posuere magna nibh et nibh. Nunc porttitor neque eu arcu volutpat, vel facilisis mi scelerisque.
Etiam fermentum orci quis pharetra pretium. In tincidunt sem enim. In in consequat arcu. Integer tempus dictum magna sed sollicitudin.


Portfolio:
http://your.portfolio
GitHub:
https://github.com/user
    """

    print("Iniciando servidor SMTP.")
    # Set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(my_address, password)
    print("Logueado en servidor SMTP.")
    #For each contact, send the email:
    for email in formatted_emails:
        # Create message
        msg = MIMEMultipart()

        # Setup the parameters of the message
        msg['From']=my_address
        msg['To']=email
        msg['Subject']=message_title

        # Add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # Add pdf attachment
        attachment = MIMEBase('application', "octet-stream")
        attachment.set_payload(open("curriculum_vitae.pdf", "rb").read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment; filename="curriculum_vitae.pdf"')
        msg.attach(attachment)

        # Send the message via the server set up earlier
        s.send_message(msg)
        print("Email enviado a {}".format(email))
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()

print("******  Listo, todos los mensajes fueron enviados!  ******")
