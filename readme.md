This repo contains the modules requred to run a solution to the Unite Ideas challenge: #LinksSDGs
See details of the challenge at: https://unite.un.org/ideas/content/linkssdgs-natural-language-processing-and-data-visualization-challenge

See the live demo at: http://LinksSDGs.bebemama.org:8080/


To implement this solution:

0) start a virtual Ubuntu server (14.04)

1) Get setup script $ wget https://raw.githubusercontent.com/jmmnn/linksSDGs/V3/server_update.py

3)  run it: $ python server_update.py

4) Get installation script $ wget https://raw.githubusercontent.com/jmmnn/linksSDGs/V3/server_installs.py

5) Run it: python server_installs.py

6) Bring the entire solution to your server: $ git clone https://github.com/jmmnn/linksSDGs.git

7) Start solr: $ python linksSDGs/start_solr.py

8) Install the Webserver, only the first time: 
  $sudo apt-get install gunicorn  
  $sudo pip install -U solrpy  
  $sudo pip install Flask  

8) Start the webserver:  
  $ cd linksSDGs/Webapp_v_2_4/  
  $ nohup gunicorn -b 0.0.0.0:8080 index:app &  

9) #Your APP will be available at:  
from terminal: $ curl http://localhost:8080/  

10) #Your Apache Solr Server will be available at: 
from terminal: $ curl http://localhost:8081/solr  

If both WebApp and Solr are working fine from your terminal, try from an outside web browser:  

Webapp: from a remote web browser (this shuold fail because of your server's firewall): http://yourServerPublicIP:8080/  
Solr: from a remote web browser (this shuold fail because of your server's firewall): http://yourServerPublicIP:8081/solr  

Both of these shuld normally fail. This is because your cloud provider usually keeps servers closed from external acces by default.
At this point, you need to configure your cloud servers "security rules" or "security groups" to open port 8080 to everyone.  

Usually this is done by adding a Custom TCT rule which enables access to the port range 8080/8080 from originating IP addresses "0.0.0.0/0"  

11) For additional security in your own box. Go back to the terminal and Enable the Ubuntu firewall to allow access only to the webapp (not solr).
$ cd ..
$ python security_setup.py  

Test that you can still access the webapp, but not Solr.

----- You are done ------

For more instructions see the readme.md file within each module.

All original work is licenced GPL 3.0. But the project relies heavily on other tools, all of which are opensource tools under their respective license.

---- In case of troubel -----  

## Use this if the service is down, then test.

Use a terminal connection to your Server. 

-Test the Solr server is running:  
  $ curl http://localhost:8081/solr
  
#Test the Web application is running:  
  $ curl http://localhost:8080/

If Solr down:  
  $ python linksSDGs/start_solr.py

If Webapp is down:  
  $ cd linksSDGs/Webapp_v_2_4/    
  $ nohup gunicorn -b 0.0.0.0:8080 index:app &


# Deprecated code, don't use this anymore:
Enable a monitor script which will restart the webapp it it fails: $ nohup python linksSDGs/webapp_monitor.py &
