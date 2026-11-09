import urequests, json

class Firebase:
    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}
        
    def put(self, path, data):
        url = self.url + path + ".json" 
        response = urequests.put(url, data=json.dumps(data), headers=self.headers)
        print("Status:", response.status_code)
        print("Response:", response.text)
        response.close()
        
    def add_to(self, path, data):
        url = self.url + path + ".json"
        response = urequests.post(url, data=json.dumps(data), headers=self.headers)
        print("Status:", response.status_code)
        print("Response:", response.text)
        response.close()
        
    def get(self, path):
        url = self.url + path + ".json"
        response = urequests.get(url)
        print("Status:", response.status_code)
        print("Response:", response.text)
        data = response.json()
        response.close()
        return data
    
    def delete(self, path):
        url = self.url + path + ".json"
        response = urequests.delete(url)
        print("Status:", response.status_code)
        print("Response:", response.text)
        response.close()
