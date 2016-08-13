This repo contains the modules requred to run a solution to the Unite Ideas challenge: #LinksSDGs
See details of the challenge at: https://unite.un.org/ideas/content/linkssdgs-natural-language-processing-and-data-visualization-challenge

See the live demo at: http://LinksSDGs.bebemama.org:8080/


To implement this solution:

0) start a virtual Ubuntu server

1) Get setup script $ wget https://raw.githubusercontent.com/jmmnn/linksSDGs/V3/server_update.py

3)  run it: $ python server_update.py

4) Get installation script $ wget https://raw.githubusercontent.com/jmmnn/linksSDGs/V3/server_installs.py

5) Run it: python server_installs.py

6) Bring the entire solution to your server: $ git clone https://github.com/jmmnn/linksSDGs.git

7) Start solr: $ python linksSDGs/start_solr.py

8) Start the Webapp:
#install gunicorn  the first time
$sudo apt-get install gunicorn

## Use this if the service is down, then test.
$ cd linksSDGs/Webapp_v_2_4/

$ nohup gunicorn -b 0.0.0.0:8080 index:app &

### old script don't use anymore $ python linksSDGs/start_webapp.py

9) #Your APP will be available at: http://yourServer:8080/

10) #Your Apache Solr Server will be available at: http://yourServer:8081/solr

If both are working fine, for security:

11) Enable the firewall to allow access only to the webapp $ python linksSDGs/security_setup.py

Test that you can still access the webapp, but not Solr.

12) 
# don't enable this anymore:
Enable a monitor script which will restart the webapp it it fails: $ nohup python linksSDGs/webapp_monitor.py &

For instructions see the readme.md file within each module.

All original work is licenced GPL 3.0. But the project relies heavily on other tools, all of which are opensource tools under their respective license.
