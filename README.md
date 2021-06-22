# finalproject
## KKBOX OpenAPI Application
## Build process 
### Environment
* python3.7.8
![image](https://github.com/irenesu2000/finalproject/blob/main/image/env.PNG)
### Installation
* 安裝requests套件:pip install requests 
* 安裝flask:pip install flask
## Introduction
本專案運用KKBOX OpenAPI來取得即時音樂排行榜資料並將其顯示至網頁供使用者搜尋排行榜歌曲

## Details of the approach
主要架構分為三大步驟
* 取得ID,Secret以獲取憑證
* API存取獲得資料
* 將資料顯示至前端給使用者搜尋  
### 申請
在存取KKbox的資料資料前需要取得Access Token才能進行每次的API呼叫  
因此需先至KKbox developer頁面申請帳號 ( https://developer.kkbox.com/#/)
接著透過requests套件的post方法取得憑證資料
### API存取
取得之後我們可以獲得json檔的憑證,將其轉換成dict或是list便可取用,則可開始存取API
![image](https://github.com/irenesu2000/finalproject/blob/main/image/Json.PNG)
透過 /charts API網址來取得排行榜資料,在 HTTP Header 中加入 Authorization: Bearer {YOUR_ACCESS_TOKEN}便可取得排行榜編號   
再透過/charts/:chart_id/tracks API網址可獲得排行榜內歌曲資訊
### 顯示至前端
將資料透過python flask套件中的render_template,可將變數傳遞至html,之便能運用資料

## Results
### Run
需創建個與start.py同層之資料夾"templates"並將"home.html"放置其中,便可執行
執行完會出現網址 按ctrl+c便可前往

![image](https://github.com/irenesu2000/finalproject/blob/main/image/vscode.png)  
### 使用者頁面
![image](https://github.com/irenesu2000/finalproject/blob/main/image/result.png)  
 
### 可自行搜尋歌曲  
![image](https://github.com/irenesu2000/finalproject/blob/main/image/search.png)  

### 複製網址可前往於kkbox相對應歌曲
![image](https://github.com/irenesu2000/finalproject/blob/main/image/link.png)

## References
### KKBOX OPENAPI
* (https://github.com/KKBOX/OpenAPI-Python)  
* (https://docs-zhtw.kkbox.codes/#overview)  
*  (https://www.learncodewithmike.com/2020/02/python-kkbox-open-api.html)  
*  (https://github.com/KKBOX/OpenAPI-JavaScript)  
              
