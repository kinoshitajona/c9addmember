from django.shortcuts import render
from django.http import HttpResponse
from adduser import add_user
import os, re

# Create your views here.
def join(req):
    if not 'C9_USER_NAME' in os.environ or not 'C9_PASSPHRASE' in os.environ or not 'C9_TEAM_NAME' in os.environ:
        return HttpResponse("ERROR: Need environment variables C9_USER_NAME and C9_PASSPHRASE and C9_TEAM_NAME set")
    return render(req, "index.html")

def send_invite(req):
    if not 'C9_USER_NAME' in os.environ or not 'C9_PASSPHRASE' in os.environ or not 'C9_TEAM_NAME' in os.environ:
        return HttpResponse("ERROR: Need environment variables C9_USER_NAME and C9_PASSPHRASE and C9_TEAM_NAME set")
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", req.POST['email']):
        return HttpResponse("ERROR: Please enter a valid email address.")
    result = add_user(req.POST['email'])
    if result:
        return HttpResponse("SUCCESS! Your invite has been sent!")
    else:
        return HttpResponse("Oops! Looks like there was a problem... check your inbox to see if the invite came or not... if not, inform your teacher.")