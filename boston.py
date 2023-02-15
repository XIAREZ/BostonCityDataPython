import json
import urlib.request
import urlib.parse
import urlib.error

url = "https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json" 
uh = urlib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
#print type of the data
print(type(data))
#convert the data to json
js = json.loads(data)
print(type(js))
data = js["data"]
print(data[0])