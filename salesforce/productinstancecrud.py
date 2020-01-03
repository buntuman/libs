'''
This file contains methods to perform crud operation of sf instance
'''


# import slaesforce login credentials
import config
from simple_salesforce import Salesforce
import json

class ProductInstance:
    def __init__(self):
        try:
            self.connection = Salesforce(config.username,config.password,config.security_token)
            self.error = None
        except:
            self.connection = None
            self.error = "Invalid Credentials"

    def where(self,field,value):
        desc = self.connection.Product_Instance__c.describe()
        field_names_list = [field['name'] for field in desc['fields']]
        part = {name:None for name in field_names_list}
        field_names = ",".join(field_names_list)
        soql = "SELECT %s FROM Product_Instance__c WHERE %s = '%s'"%(field_names,field,value)
        results = self.connection.query_all(soql)
        self.count = results['totalSize']
        self.records = list()
        for record in results['records']:
            for key in field_names_list:
                part[key] = record[key]
            self.records.append(part)
            print(json.dumps(self.records))

    def getError(self):
        return self.error

