This repo contains the modules requred to run a solution to the Unite Ideas challenge: #LinksSDGs
See details of the challenge at: https://unite.un.org/ideas/content/linkssdgs-natural-language-processing-and-data-visualization-challenge

See the live demo at: http://192.169.173.168:8080/  


To implement this solution:

0) start a virtual Ubuntu server

1) Get setup script $ wget https://raw.githubusercontent.com/jmmnn/linksSDGs/V3/server_update.py

3)  run it: $ python server_update.py

4) Get installation script $ wget https://raw.githubusercontent.com/jmmnn/linksSDGs/V3/server_installs.py

5) Run it: python server_installs.py

6) Bring the entire solution to your server: $ git clone https://github.com/jmmnn/linksSDGs.git

7) Start solr: $ python linksSDGs/start_solr.py

8) Start the Webapp $ python linksSDGs/start_webapp.py

For instructions see the readme.md file within each module.

All original work is licenced GPL 3.0. But the project relies heavily on other tools, all of which are opensource too under their respective license.

JMN