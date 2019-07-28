from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpRequest  
import requests
import zeep
from zeep import Client, Settings
from zeep import xsd

def index(request):
	response = 'index output text'
	return HttpResponse(response)

def getcontainedequipment(request):
	wsdl = 'http://172.28.40.24:9999/mtosi/EquipmentInventoryRetrieval?wsdl'
	client = zeep.Client(wsdl=wsdl)
	
	header_element = client.get_element('ns2:header')	
	ehRef_element = client.get_element('ns0:getContainedEquipmentRequest')	
	ObjectTypeType = client.get_type('ns3:ObjectTypeType')
	RelativeDistinguishNameType = client.get_type('ns4:RelativeDistinguishNameType')
	NamingAttributeType = client.get_type('ns4:NamingAttributeType')	
	#headers
	activityName='getContainedEquipment'
	msgName='getContainedEquipmentRequest'
	msgType='REQUEST'
	senderURI='Infinera/XIS-OS'
	destinationURI='Infinera/XIS-OS'
	communicationPattern='SimpleResponse'
	communicationStyle='RPC'
	#rdn_body
	md_type = ObjectTypeType('MD')
	md_value = xsd.String()('Infinera/XIS')
	me_type = ObjectTypeType('ME')
	me_value = xsd.String()('MA4616070129')
	eh_type = ObjectTypeType('EH')
	eh_value = xsd.String()('/shelf=2')			

	rdn_object = [RelativeDistinguishNameType(type=md_type, value=md_value),RelativeDistinguishNameType(type=me_type, value=me_value), RelativeDistinguishNameType(type=eh_type, value=eh_value)]
	rdn_body = NamingAttributeType(rdn=rdn_object)
	mtopHeader = header_element(activityName=activityName, msgName=msgName, msgType=msgType, senderURI=senderURI, destinationURI=destinationURI, communicationPattern=communicationPattern, communicationStyle=communicationStyle)	
	soap_response = client.service.getContainedEquipment(ehRef = rdn_body, _soapheaders=[mtopHeader])
	return HttpResponse(soap_response.body.eoh)

