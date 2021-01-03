docker images | sed 1d > ./../files/dockerimages.txt
docker ps | sed 1d | tr '"' ' '> ./../files/dockerrunningcontainers.txt
docker ps -a | sed 1d | tr '"' ' ' > ./../files/dockerallcontainers.txt
