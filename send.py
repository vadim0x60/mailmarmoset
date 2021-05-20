import markdownmail
from braceexpand import braceexpand
import yaml

from deepmerge import always_merger
deep_merge = always_merger.merge

import os
import sys
from string import Template

smtp_email = os.environ['EMAIL']
smtp_pwd = os.environ['EMAIL_PWD']
smtp_url, smtp_port = os.environ['EMAIL_SMTP'].split(':')

def send_email(to, subject, template, insert):
    template_path = os.path.join(sys.path[0], 'templates', template)
    with open(template_path) as f:
        text=Template(f.read()).substitute(**insert)

    if type(to) == str:
        to = [to]

    email = markdownmail.MarkdownMail(
        from_addr=smtp_email,
        to_addr=[address.strip() for addressoid in to for address in braceexpand(addressoid)],
        subject=subject,
        content=text
    )

    email.send(smtp_url, login=smtp_email, password=os.environ['EMAIL_PWD'], port=smtp_port, tls=True)

def send_blast(config):
    if 'branches' in config:
        branches = config['branches']
        del config['branches']

        for branch_config in branches:
            send_blast(deep_merge(config, branch_config))
    else:
        send_email(**config)

with open('blast.yml') as f:
    send_blast(yaml.safe_load(f))
os.rename('blast.yml', 'sent_blast.yml')