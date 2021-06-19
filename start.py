import requests
from flask import Flask
from flask import render_template
def get_access_token():
    #API網址    
    url = "https://account.kkbox.com/oauth2/token" 
    
    #標頭
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "account.kkbox.com"
    }

    #參數
    data = {
        "grant_type": "client_credentials",
        "client_id": "0eca2b5ae11be036975e15345f738982",
        "client_secret": "83367836490368d23f7be1be52fe2cb1"
    }

    access_token = requests.post(url, headers=headers, data=data)
    return access_token.json()["access_token"]

    # 取得各種音樂排行榜列表
def get_charts():
    #取得存取憑證
    access_token = get_access_token() 

   #取得音樂排行榜列表API網址
    url = "https://api.kkbox.com/v1.1/charts"

    #標頭
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token  #帶著存取憑證
    }

    #參數
    params = {
        "territory": "TW"  #台灣領域  
    }

    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    
def get_charts_tracks(chart_id):
    #存取憑證
    access_token = get_access_token() 

    #取得音樂排行榜列表中的歌曲API網址
    url = "https://api.kkbox.com/v1.1/charts/" + chart_id + "/tracks"

    #標頭
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token
    }

    #參數
    params = {
        "territory": "TW"  #台灣領域
    }
   
    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    gogo(result)

app = Flask(__name__)    
def gogo(result):
    @app.route("/")
    def home():
        return render_template('home.html',result=result)   
    

def user() :
    get_charts()
    get_charts_tracks('LZPhK2EyYzN15dU-PT')
    

if __name__ == '__main__':
    user()
    app.run() 
    
   



