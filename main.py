##########################
# Python 3.x Example
##########################

# package used to execute HTTP POST request to the API
import json
import urllib.request

# API endpoint
API = "https://api.sec-api.io?token=" + "b8ed79ca4cae0facef76323d757a99865f0d5402852b80538acee9c31189040b"

# define the filter parameters you want to send to the API
payload = {
  "query": { "query_string": { "query": "cik:1707359 AND (formType:D OR formType:C) AND formType:(NOT \"C-AR\") AND formType:(NOT \"C-U\")" } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

# format your payload to JSON bytes
jsondata = json.dumps(payload)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes

# instantiate the request
req = urllib.request.Request(API)

# set the correct HTTP header: Content-Type = application/json
req.add_header('Content-Type', 'application/json; charset=utf-8')
# set the correct length of your request
req.add_header('Content-Length', len(jsondataasbytes))

# send the request to the API
response = urllib.request.urlopen(req, jsondataasbytes)

# read the response
res_body = response.read()
# transform the response into JSON
filings = json.loads(res_body.decode("utf-8"))

# print JSON
print(filings)