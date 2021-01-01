import requests
import threading
import webapi
import wrapper

def startWebserver():
	webapi.app.run() 

def startGraph():
	wrapper.app.run_server()

x = threading.Thread(target=startWebserver)
y = threading.Thread(target=startGraph)
x.start() #http://127.0.0.1:5000/
y.start() #http://127.0.0.1:8080/
print("Started threads.")
