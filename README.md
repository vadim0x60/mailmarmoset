# Mail marmoset

## Why

Ever used [mailchimp](https://mailchimp.com/)? 
This library is to mailchimp what [marmoset](https://en.wikipedia.org/wiki/Marmoset) is to a chimp - a smaller, cuter and simpler version of an overgrown monstrosity.
A fully functioning email campaign tool built with 31 lines of Python.

## How

*Clone* this repository

```
git clone https://github.com/vadim0x60/mailmarmoset
```

Pick a template or write one yourself.
A template is a [markdown](https://www.markdownguide.org/) file with an email you want to send to multiple people that you place in `templates` folder.
The template can contain _personalization variables_ - each `$variable` will be replaced with personalized information for each receipient.
See `templates/monkeys.md` for example.

Write `blast.yml` - this is a file that describes who is going to receive your email blast. For example:

```
template: monkeys.md
victims:
  -
    to: 'alicechimpfan@email.com'
    subject: 'Chimps for sale!'
    with:
      name: 'Alice'
      url: 'monkey.example.com'
  -
    to: ['{robert1,robert2}@email.com', 'robert3@otheremail.com']
    subject: 'Monkeys for sale!'
    with:
      name: 'Bob'
      url: 'monkey.example.com'
  -
    to: 'charleymarmosetenjoyer@email.com'
    subject: 'Marmosets for sale!'
    with:
      name: 'Charley'
      url: 'monkey.example.com'
```

Every victim entry has to contain `to` (an email address or a list of addresses, [brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html) is supported), `subject` and `with` (substitutions for all personalization variables for this victim).

*Connect* your email account. All the emails will be sent from your email account. To connect it you need to set `EMAIL`, `EMAL_PWD` and `EMAIL_SMTP` environment variables: `EMAIL_SMTP` is your [SMTP server address](https://knowledge.hubspot.com/email-notifications/how-can-i-find-my-email-servers-imap-and-smtp-information) in `url:port` format, `EMAIL` is username `EMAL_PWD` is password.

*Run* 

```
python send.py
```

The emails will be sent. `blast.yml` will be renamed to `sent_blast.yml` so that you don't accidentally send it twice.