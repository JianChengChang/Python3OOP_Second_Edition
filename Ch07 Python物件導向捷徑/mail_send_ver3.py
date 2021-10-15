import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

def send_email(subject, message, from_addr, *to_addrs, host='localhost', port=1025, headers=None):
    headers = {} if headers is None else headers
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value
    
    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()

class MailingList:
    '''管理發送郵件的郵件地址群組'''
    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)
    
    def add_to_group(self, email, group):
        self.email_map[email].add(group)
    
    def emails_in_groups(self, *groups):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails
    
    def send_mailing(self, subject, message, from_addr, *groups, headers=None):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, headers=headers)

    def save(self):
        with open(self.data_file, 'w') as file:
            for email, groups in self.email_map.items():
                file.write(
                    f"{email} {','.join(groups)}\n"
                )
    
    def load(self):
        self.email_map = defaultdict(set)
        #try:
        with open(self.data_file) as file:
            for line in file:
                email, groups = line.strip().split(' ')
                groups = set(groups.split(','))
                self.email_map[email] = groups
        #except IOError:
            #pass
    
    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()

if __name__ == '__main__':
    m = MailingList('addresses_db')
    m.add_to_group("friend1@example.com", "friends")
    m.add_to_group("family1@example.com", "friends")
    m.add_to_group("family1@example", "family")
    m.add_to_group("pro1@example.com", "professional")
    m.save()

    with MailingList('addresses_db') as m1:
        m1.add_to_group("friend2@example.com", "friends")
        m1.send_mailing("What's up", "Hey friends, how's it going", "me@example.com", 'friends')
    
