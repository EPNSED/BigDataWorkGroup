#!/usr/bin/python

#Copyright [2016] [Neranjan Suranga Edirisinghe, epnsed@gmail.com]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


import json
import sys
import urllib2
import requests
import csv
import unicodedata

eventbrite_data = open('./FullData.csv', 'w')
# Quick Start guid for the Eventbrite API https://www.eventbrite.com/developer/v3/quickstart/
# Create API key and replace ******* with the key
# How to generate API key https://www.eventbrite.com/support/articles/en_US/How_To/how-to-locate-your-eventbrite-api-user-key?lg=en_US
response = requests.get("https://www.eventbriteapi.com/v3/events/search/?token=*************")

#Open a file to write csv data
recordwriter = csv.writer(eventbrite_data)
count = 0
#For each page in the response do 
for pagecount in range(response.json()["pagination"]["page_count"]):
        #Get new page, here you can customize with different expansions : https://www.eventbrite.com/developer/v3/reference/expansions/
	response = requests.get("https://www.eventbriteapi.com/v3/events/search/?expand=venue,category&token=GY4LYI2GKX2WT4I6Y7PB&page="+str(pagecount),verify = True,)
        for record in range(len(response.json()['events'])):
		#read through the input data structure and populate the output data structure
                json_data = {}
		json_data['id']=response.json()['events'][record]['id']
                json_data['time_zone']=response.json()['events'][record]['start']['timezone']
                json_data['start_time']=response.json()['events'][record]['start']['local']
                json_data['online_event'] = response.json()['events'][record]['online_event']
                json_data['is_series'] = response.json()['events'][record]['is_series']
                json_data['category_id'] = response.json()['events'][record]['category_id']
                json_data['capacity']=response.json()['events'][record]['capacity']
                json_data['name'] = response.json()['events'][record]['name']['text']
                json_data['organizer_id'] =response.json()['events'][record]['organizer_id']
                #some times venue is a NULL object, so we need to specifically handle it.
		if response.json()['events'][record]['venue'] is None :
			json_data['postal_code'] = None
                	json_data['latitude'] = None
        	        json_data['longitude'] = None
	                json_data['state'] = None
                	json_data['city'] = None
		else :
			json_data['postal_code'] = response.json()['events'][record]['venue']['address']['postal_code']
			json_data['latitude'] = response.json()['events'][record]['venue']['address']['latitude']
			json_data['longitude'] = response.json()['events'][record]['venue']['address']['longitude']
			json_data['state'] = response.json()['events'][record]['venue']['address']['region']
			json_data['city'] = response.json()['events'][record]['venue']['address']['city']
		#handling NULL objects 
		if response.json()['events'][record]['category'] is None :
			json_data['category'] = None
		else :
			json_data['category'] = response.json()['events'][record]['category']['name']
		
		#json_recode["data"].append(json_data)
		#This may not the best way to do this :) but we are writing these data in to json and then reading back with proper formatting using python library calls
		with open('result.json', 'w') as fp:
			#data = json.dump(json_data,fp,indent=4, sort_keys=True, separators=(',', ':'))
			data = json.dump(json_data,fp,separators=(',', ':'))

		with open('result.json', 'r') as fp:
			test_json=json.load(fp)
		# Now write this back to csv file so that we can read with Hadoop eco system easilly, again this is not the way to do this, but this works :)
		if count == 0:
                	header = test_json.keys()
                	recordwriter.writerow(header)
			x=[]
			for s in test_json.values():
                		if isinstance(s, str):
        				x.append(s.replace(",", " ").replace(";", " "))
    				elif isinstance(s, unicode):
        				#dealing with some unicode stuff 
					x.append(unicodedata.normalize('NFKD',s.replace(",", " ").replace(";", " ")).encode('ascii','ignore'))
    				else:
        				x.append(s)
			recordwriter.writerow(x)
                	count += 1
        	else :
                	x=[]
                        for s in test_json.values():
                                if isinstance(s, str):
                                        x.append(s.replace(",", " ").replace(";", " "))
                                elif isinstance(s, unicode):
                                        x.append(unicodedata.normalize('NFKD', s.replace(",", " ").replace(";", " ")).encode('ascii','ignore'))
                                else:
                                        x.append(s)
                        recordwriter.writerow(x)
print test_json.keys()
eventbrite_data.close()
