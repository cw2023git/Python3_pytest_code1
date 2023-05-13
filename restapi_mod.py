from hashlib import sha1
import json
import requests

class Restapi(object):
    def __init__(self,userName,password,platformName,ip):
        self.userName = userName
        self.password = password
        self.platformName = platformName
        self.ip = ip

    def auth3(self,userName, password, desc, rand):
        concat = str(rand) + password + "sangfor3party" + userName + desc
        return sha1(concat.encode('utf-8')).hexdigest()

    def get_token(self):
        url = "https://" + self.ip + ":7443/sangforinter/v1/auth/party/login"
        data = {
                "userName":self.userName,
                "rand":74,
                "clientProduct":"",
                "clientVersion":"",
                "clientId":0,
                "desc":"",
                "auth":self.auth3(self.userName,self.password,"","74"),
                "platformName":self.platformName
        }
        try:
            data = json.dumps(data)
            r = requests.post(url,data,verify=False,timeout=30)
            return json.loads(r.content)["data"]["token"]
        except Exception as e:
            # print str(e)
            print(str(e))
            return False

    def get_data(self,fromTime,toTime,datatype):
        token = self.get_token()
        if not token:
            # print "get token failed"
            print("get token failed")
            return False
        url = "https://%s:7443/sangforinter/v1/data/%s?token=%s&fromActionTime=%s&toActionTime=%s&maxCount=%s"%(self.ip,datatype,token,str(fromTime),str(toTime),2000)
        r = requests.get(url,verify=False,timeout=30 )
        data = r.content
        return data

if __name__ == "__main__":
    app = Restapi('admin','admins@123','安全平台本地测试2',"192.168.1.201")
    # print app.get_data(0,999999999999,"ipgroup")
    print(app.get_data(0,999999999999,"ipgroup"))
