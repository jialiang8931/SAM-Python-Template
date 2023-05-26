import requests

class LineNotify:
    def __init__(self,):
        self.linkAPI = "https://notify-api.line.me/api/notify"
        return
    
    def publish(self, token, message, img=None):
        if message == '': return {"status": "empty message"}

        payload = {'message': message}
        image = {'imageFile' : requests.get(img).content} if (img != None) else {'imageFile' : None}
        
        headers = {
            "Authorization": "Bearer " + token
        }

        response = requests.post(self.linkAPI, headers=headers, params=payload, files=image)
        return {
            "status_code": response.status_code, 
        }

broadcaster = LineNotify()
