# docker-dashboard

##Project Description

###Author : Chetan SH

###Project Name : Docker Dashboard 

###Version : 1.2.0

###Purpose
This project is called Docker Dashboard, because it displays
the status of docker images,running containers and all available containers
from the system.

###Usage

1. Run the django server
2. Open the project workspace in terminal
3. Goto dashboardApp/shellscripts and Run 'dockerinfo.sh'
4. Hit localhost:8000/home/dockerdb from your browser
5. You can see the docker dashboard.
6. Run some docker commands like
    1. docker run -td ubuntu //bin/bash
    2. docker run -td centos //bin/sh
    3. docker run -td jenkins //bin/bash
    
7. Perform step 3 again and then refresh your dashboard
8. You can see the docker dashboard updating.
9. Try to crontab the shell script to run every minute
10. You'll have live docker dashboard !


### Please do help in the code improvement, if you think it needs some.
#Thank You Very Much
