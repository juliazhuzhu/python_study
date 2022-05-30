import requests
from requests.auth import HTTPDigestAuth
import json

# Replace with the correct URL
url = "http://172.24.0.118/api/rest/v2.0/login"
headers = {
			"Content-Type": "application/json",
			"Accept":"application/json"}
payload={
		"username":"xiaoye",
		"password":"48058e0c99bf7d689ce71c360699a14ce2f99774",
		"userAgent":"linphoneClients",
		"deviceSn":"12344353454455",
		"serverAddress":"172.24.0.118"}
# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
myResponse = requests.put(url, headers=headers,data=json.dumps(payload))
print (myResponse)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")

    for k,v in zip(jData.iterkeys(),jData.itervalues()): 
        print ("[%s]=" % k,v)

    #for key in jData:
     #   print (jData[key])
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()