import time
import subprocess
import requests
while True:
    try:
        r = requests.head("http://linkssdgs.bebemama.org:8080/search")
        print ('Webapp status, 200 means ok:')
        print(r.status_code)
        # prints the int of the status code:)
    except requests.ConnectionError:
        print("failed to connect")
        subprocess.call("python linksSDGs/start_webapp.py" , shell=True)
        time.sleep(60)
