import requests
import logging
import json

class SlackApi():
        def post_message_to_slack(payload):
                slack_url = "https://hooks.slack.com/services/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"
                #slack_url = "https://hooks.slack.com/services/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"
                headers = {'Content-type':'application/json', }
                slack_response = requests.post(slack_url, headers=headers, data=payload)
                #custom_response = Response( status=slack_response.status_code, content_type="application/json",headers={'X-Slack-No-Retry': 1})        
                return slack_response.status_code