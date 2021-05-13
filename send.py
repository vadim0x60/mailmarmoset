import markdownmail
from braceexpand import braceexpand
import yaml

import os
import sys
from string import Template

with open('blast.yml') as f:
    blast_config = yaml.safe_load(f)

template_path = os.path.join(sys.path[0], 'templates', blast_config['template'])
with open(template_path) as f:
    template=Template(f.read())

smtp_email = os.environ['EMAIL']
smtp_pwd = os.environ['EMAIL_PWD']
smtp_url, smtp_port = os.environ['EMAIL_SMTP'].split(':')

for victim in blast_config['victims']:
    text = template.substitute(**victim['with'])

    email = markdownmail.MarkdownMail(
        from_addr=smtp_email,
        to_addr=[address.strip() for to in victim['to'] for address in braceexpand(to)],
        subject=victim['subject'],
        content=text
    )
        
    email.send(smtp_url, login=smtp_email, password=os.environ['EMAIL_PWD'], port=smtp_port, tls=True)
os.rename('blast.yml', 'sent_blast.yml')