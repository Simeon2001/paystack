import requests
from requests.structures import CaseInsensitiveDict
import json

#https://af03ae84ce73.ngrok.io
api_token = 'sk_test_64c57f0f1626abd2c27f7f96c379f199e9e835ea'
headers = CaseInsensitiveDict()

headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer {0}".format(api_token)

#to generate link to deposit cash
def charge (em,am):

    p_url = 'https://api.paystack.co/transaction/initialize'
    info = {
  
        "email": em,
  
        "amount": am
    }
    data = json.dumps(info,indent=2)
    
    res = requests.post(p_url,headers=headers,data=data)
    v = (res.json())
    return v

#total amount received on account 
def total_amount ():
    p_url = 'https://api.paystack.co/transaction/totals'
    res = requests.get(p_url,headers=headers)
    v = (res.json())
    return v

#create customer
def customer (em,first_name,last_name):
    p_url = 'https://api.paystack.co/customer'
    info = {
  
        "email": em,
  
        "first_name": first_name,

        "last_name": last_name
    }
    data = json.dumps(info,indent=2)
    
    res = requests.post(p_url,headers=headers,data=data)
    v = (res.json())
    return v

#create account number for customer
def nuban (customer_id):
    p_url = 'https://api.paystack.co/dedicated_account'
    info = {
  
        "customer": customer_id,
  
        "preferred_bank": "wema-bank"
    }
    data = json.dumps(info,indent=2)
    
    res = requests.post(p_url,headers=headers,data=data)
    v = (res.json())
    return v

#create account send money to other account 
def send_to (name,account_no,bank_code):
    p_url = 'https://api.paystack.co/transferrecipient'
    info = {'type':'nuban','name':name,'description':'payment from compaym','account_number':account_no,'bank_code':bank_code,'currency':'NGN'}
    res = requests.post(p_url,headers=headers,data=info)
    v = (res)
    return v







