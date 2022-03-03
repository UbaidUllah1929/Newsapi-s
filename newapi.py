from flask import Flask,jsonify,request
import requests

app = Flask(__name__)

@app.route('/newsapi', methods=['GET'])
def newsapi():
        base_url="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=9333624aa1fb4278950034f25ae3d676"
        res1=requests.get(base_url,
                                 headers={"Authorization":"Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ",
                                           "Accept":"application/json"}).json()
        
    
        data=res1["articles"][0]["source"]        
        
        headlines=res1["articles"][0]["title"]
        url_data=res1["articles"][0]["url"]
        return jsonify({"headlines":headlines,"link":url_data,"source":data}) 
@app.route('/reddit', methods=['GET'])
def reddit():
    base_url="https://api.reddit.com/new"
    res1=requests.get(base_url,
                             headers={"Authorization":"Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ",
                                       "Accept":"application/json"}).json()
    
    url_news=res1["data"]["children"][0]["data"]["url"]
    headlines=res1["data"]["children"][0]["data"]["title"]
    return jsonify({"headlines":headlines,"link":url_news})    
@app.route('/news', methods=['GET'])
def news():
    
    query=request.args['query']
    base_url="https://newsapi.org/v2/everything?q={}&from=2022-03-03&sortBy=popularity&apiKey=9333624aa1fb4278950034f25ae3d676"
    base_url=base_url.format(query)
    query=base_url
    res1=requests.get(query,
                             headers={"Authorization":"Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ",
                                       "Accept":"application/json"}).json()
    data=res1["articles"][0]["source"]        
   
    headlines=res1["articles"][0]["title"]
    url_data=res1["articles"][0]["url"]
    return jsonify({"headlines":headlines,"link":url_data,"source":data}) 
@app.route('/news1', methods=['GET'])  
def news1():
    
    query=request.args['query']
    base_url="https://api.reddit.com/search?q={}"
    base_url=base_url.format(query)
    query=base_url
    res1=requests.get(query,
                             headers={"Authorization":"Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ",
                                       "Accept":"application/json"}).json()
    url_news=res1["data"]["children"][0]["data"]["url"]
    headlines=res1["data"]["children"][0]["data"]["title"]
    return jsonify({"headlines":headlines,"link":url_news})
     
if __name__ == "__main__":
    app.run(debug=True,port=(100))