import configparser
import os
import imaplib
import email
import re

# Function to connect to the email server and fetch emails from a specific sender
def fetch_emails(email_user, email_pass, specific_sender):
    mail = imaplib.IMAP4_SSL(host = 'imap-mail.outlook.com', port = 993)  # Change to your email provider's IMAP server
    mail.login(email_user, email_pass)
    mail.select('inbox')
    
    # Search for emails from the specific sender
    result, data = mail.search(None, f'FROM "{specific_sender}"')
    email_ids = data[0].split()
    
    emails = []
    for e_id in email_ids:
        result, msg_data = mail.fetch(e_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        emails.append(msg)
    
    mail.logout()
    return emails

# Function to extract journey cost from the email body
def extract_cost(body):
    # Assuming the cost is mentioned in a format like "Cost: $50" or "Total: $50"
    cost_match = re.search(r'Cost:\s*\$?(\d+\.?\d*)|Total amount:\s*\$?(\d+\.?\d*)', body)
    if cost_match:
        return cost_match.group(1) or cost_match.group(2)
    return None

if __name__ == '__main__':

    root_dir = os.path.dirname(os.path.realpath(__file__))

    config = configparser.ConfigParser()
    config.read('config.ini')

    email_user = config['EMAIL']['user']
    email_password = config['EMAIL']['password']

    specific_sender = 'auto-confirm@info.thetrainline.com'

    emails = fetch_emails(email_user, email_password, specific_sender)

    print(len(emails))
