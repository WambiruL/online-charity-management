from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_usaidizi_email(name,receiver):
    # Creating message subject and sender
    subject = 'Thank you for being a part of USAIDizi'
    sender = 'ernest.mucheru@student.moringaschool.com'

    #passing in the context vairables
    text_content = render_to_string('email/usaidizi.txt',{"name": name})
    html_content = render_to_string('email/usaidiziemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def donated_email(donor,receiver):
     # Creating message subject and sender
    subject = 'USAIDizi appreciates your donation'
    sender = 'ernest.mucheru@student.moringaschool.com'

     #passing in the context vairables
    text_content = render_to_string('email/donate_email.txt',{"donor": donor})
    html_content = render_to_string('email/donate_email.html',{"donor": donor})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def approve_request(admin,receiver):
    subject = 'You have just updated the approval status of a funding request'
    sender = 'ernest.mucheru@student.moringaschool.com'

     #passing in the context vairables
    text_content = render_to_string('email/approval.txt',{"admin": admin})
    html_content = render_to_string('email/approval.html',{"admin": admin})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def make_request(ngo,receiver):
    subject = 'Request made. Pending approval.'
    sender = 'ernest.mucheru@student.moringaschool.com'

     #passing in the context vairables
    text_content = render_to_string('email/request.txt',{"ngo": ngo})
    html_content = render_to_string('email/request.html',{"ngo": ngo})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()