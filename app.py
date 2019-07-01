#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Run one by one

import requests
import json

# Organization information
# This route returns information on the current authenticated user.
def get_userinfo():
    url = "https://api.gandi.net:0/v5/organization/user-info"
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers)
    data = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))

# Search organization info
def get_org():
    url = "https://api.gandi.net:0/v5/organization/organizations"
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers)
    data = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))

# Get billing information
def get_billing():
    url = "https://api.gandi.net:0/v5/billing/info/a8c260de-c114-11e7-b198-00163ec31f40"
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers)
    data = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))

def get_billing2():
    url = "https://api.gandi.net:0/v5/billing/info"
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers)
    data = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))

# Domain availability
def check_availability():
    url = "https://api.gandi.net/v5/domain/check"
    domainname = input("Enter a domain name: ") # Give a if condition to show an error message if there are spaces or any other characters that we can't accept
    querystring = {"name":domainname}
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))

# Domain availability
def check_availability():
    url = "https://api.gandi.net/v5/domain/check"
    domainname = input("Enter a domain name: ")
    tlds = {1: ".com", 2: ".net", 3: ".org", 4: ".io", 5: ".info", 6: ".jp"}
    for key in tlds:
        querystring = {"name":domainname + tlds[key]}
        headers = {'authorization': 'Apikey <your api key>'}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        data_json = json.loads(data)
        print(json.dumps(data_json, indent=2))


# List available TLDs
def list_available_tlds():
    url = "https://api.gandi.net/v5/domain/tlds"
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers)
    data = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))

#Domain create and list: List out the domain names you already own
def domain_create():
    url = "https://api.gandi.net/v5/domain/domains"
    domainname = input("Enter a domain name: ")
    querystring = {"fqdn":domainname + ".*"}
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))



def list_available_tlds():
    url = "https://api.gandi.net/v5/domain/tlds"
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers)
    print(response.text)


# Check a specific TLD info
def check_availability():
    tld = input("Type in a TLD you want to check: ")
    url = "https://api.gandi.net/v5/domain/tlds/{}".format(tld)
    headers = {'authorization': 'Apikey <your api key>'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))

# Domain name creation - dry run
def domaincreate_dry_run():
    url = "https://api.gandi.net/v5/domain/domains"
    domainname = input("Enter a domain name: ") # Give a if condition to show an error message if there are spaces or any other characters that we can't accept
    querystring = {"name":domainname}
    payload = "{\"fqdn\":\"yamaneko.dev\",\"duration\":5,\"owner\":{\"city\":\"Paris\",\"given\":\"Alice\",\"family\":\"Doe\",\"zip\":\"75001\",\"country\":\"FR\",\"streetaddr\":\"5 rue neuve\",\"phone\":\"+33.123456789\",\"state\":\"FR-J\",\"type\":0,\"email\":\"alice@example.org\"}}"
    headers = {
    'authorization': "Apikey <your api key>",
    'content-type': "application/json",
    'dry-run': "1"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    dataj = response.text
    data_json = json.loads(data)
    print(json.dumps(data_json, indent=2))

