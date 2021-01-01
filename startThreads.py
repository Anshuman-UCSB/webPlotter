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
x.start()
y.start()
print("Started threads.")

