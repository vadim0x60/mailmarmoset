# Mail marmoset

## Why

Ever used [mailchimp](https://mailchimp.com/)? 
This library is to mailchimp what [marmoset](https://en.wikipedia.org/wiki/Marmoset) is to a chimp - a smaller, cuter and simpler version of an overgrown monstrosity.
A fully functioning email campaign tool built with 31 lines of Python.

## How

### Clone this repository

```
git clone https://github.com/vadim0x60/mailmarmoset
```

### Prepare a template

Pick a template or write one yourself.
A template is a [markdown](https://www.markdownguide.org/) file with an email you want to send to multiple people that you place in `templates` folder.
The template can contain _personalization variables_ - each `$variable` will be replaced with personalized information for each receipient.
See `templates/monkeys.md` for example.

### Configure an email blast

Write `blast.yml` - this is a file that describes who is going to receive your email blast. For example:

An email is configured with name of the `template`, `to` (an email address or a list of addresses, [brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html) is supported), `subject` and `insert` (substitutions for all personalization variables in the template).
If you need to send emails with different templates, subjects or substitutions, you can add another field, `branches`.
Branches can be infinitely nested.

For example, this `blast.yml`

```
template: monkeys.md
insert:
  url: 'monkey.example.com'
branches:
  -
    to: 'alicechimpfan@email.com'
    subject: 'Chimps for sale!'
    insert:
      name: 'Alice'
  -
    to: ['{robert1,robert2}@email.com', 'robert3@otheremail.com']
    subject: 'Monkeys for sale!'
    insert:
      name: 'Bob'
  -
    to: 'charleymarmosetenjoyer@email.com'
    subject: 'Marmosets for sale!'
    insert:
      name: 'Charley'
```

will send out 5 advertising emails, each with correcly personalized name, but with the same landing url.

### Connect your email account

All the emails will be sent from your email account. To connect it you need to set 3 environment variables: `EMAIL_SMTP` is your [SMTP server address](https://knowledge.hubspot.com/email-notifications/how-can-i-find-my-email-servers-imap-and-smtp-information) in `url:port` format, `EMAIL` is username `EMAL_PWD` is password.

### Send it

```
python send.py
```

The emails will be sent. `blast.yml` will be renamed to `sent_blast.yml` so that you don't accidentally send it twice.