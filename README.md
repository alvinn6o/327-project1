# Project 1 Docker
# Authors: Alvin Ngo, Jason Tran

# How to run Task 1
docker pull nginx:latest
docker run -d -p 8080:80 --name my-nginx nginx:latest

Check the custom web server with the command
docker run -d -p 8080:80 -v $(pwd)/index.html:/usr/share/nginx/html/index.html nginx:latest

# How to run Task 2 Server with Clients
docker-compose up --build

# Project Files
- app.py - Hello Docker script
- server.py - TCP server
- client.py - TCP client
- Dockerfile - For app.py
- Dockerfile.server - For server
- docker-compose.yaml - Multi-container setup
- index.html - Custom Nginx page
