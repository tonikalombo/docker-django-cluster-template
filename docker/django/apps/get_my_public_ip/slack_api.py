import requests
import logging
import json

class SlackApi():
        def post_message_to_slack(payload):
        		slack_domain = "XXXXX"
        		slack_service_id = "ZZZZZ"
        		slack_service_token = "YYYYYYY"
                slack_url = "https://hooks.slack.com/services/"+slack_domain+"/"+slack_service_id+"/"+slack_service_token    
                headers = {'Content-type':'application/json', }
                slack_response = requests.post(slack_url, headers=headers, data=payload)
                #custom_response = Response( status=slack_response.status_code, content_type="application/json",headers={'X-Slack-No-Retry': 1})        
                return slack_response.status_code