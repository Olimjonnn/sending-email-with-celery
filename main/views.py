from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_func


def send_mail_to_all(request, *args, **kwargs):
    username = request.user.username
    send_mail_func.delay()
    return HttpResponse("Sent")