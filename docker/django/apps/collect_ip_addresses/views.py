from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpRequest  
from uuid import getnode as get_mac

def index(request):
   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
   client_address = request.META.get('REMOTE_ADDR', None) 
   host = request.META.get('SERVER_NAME', None)
   template = loader.get_template('index.html')
   mac_address = get_mac()
   if request.META['REQUEST_METHOD'] == 'HEAD':
     output = " ---  Skipping HAProxy health checks --- "
     print(output)
     return False
   if x_forwarded_for is None:
     output = "GO AWAY!!"
     print(output)
   else:
     output = "Hello "+str(x_forwarded_for) 
   print(output)
   context = {
        'message': output,
        'node': host,
        'client': x_forwarded_for, 
        'load_balancer': client_address,
        'mac': mac_address,
    }
   return HttpResponse(template.render(context, request))
