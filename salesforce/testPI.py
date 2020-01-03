from productinstancecrud import ProductInstance

pi = ProductInstance()

if(pi.getError()):
    print("THere is an error")
else:
    print("There are no errors")
    print(pi.where("Notes__c","S4000"))
