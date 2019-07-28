from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpRequest  
import requests
from . import slack_api

def index(request):
	r = requests.get('http://jsonip.com')
	public_ip_address = r.json()['ip']	
	#slardnessage = '{"text":"'+str(public_ip_address)+'"}'
	#slack_response = slack_api.SlackApi.post_message_to_slack(slack_message)
	
	# context = {
	#   'public_ip_address': public_ip_address,
	#   'slack_response': slack_response,
	#   }
	return HttpResponse(public_ip_address)


