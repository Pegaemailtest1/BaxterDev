===========================================
1. Install Docker desktop for windows
==========================================
    https://www.docker.com/products/docker-desktop/ 
        Select Downloads for windows AMD64 option to dowload docker desktop .exe file

=========================================== 
2. Folder structure
=========================================== 

        BaxterDev/
        │
        ├── backend/
        │   └── app/
        │       ├── main.py
        │       ├── requirements.txt
        │       └── Dockerfile
        │
        └── docker-compose.yml
========================================
3. Run It All
    docker-compose up --build
=========================================

======================================
Ollama public key is: 
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILMgdR5nZ+6k9Ze81AkpA7Ikb85KWaYZ+BO2lVzRCn0T
======================================
Test Ollama is Running:
        http://ollama:11434/

    Install models into ollama server:
        Embedding MOdel:
            docker exec -it ollama ollama pull mxbai-embed-large
        Foundation Model RAG Based search:
            docker exec -it ollama ollama pull llama3



==========================
Docker Commands for AWS EC2 instance:
==========================
1. Update the System:
sudo yum update -y

2. Enable and Install Docker:
sudo amazon-linux-extras enable docker
sudo yum install -y docker


3. Start the Docker Service:
sudo service docker start

4. Test Docker Installation:
docker run hello-world

5. Check docker images:
sudo docker images

6. Pull Images:
Sudo docker pull ollama/ollama
sudo docker pull chromadb/chroma

7. check the .pem file connectivity form command prompt
ssh -i "awsec2key.pem" ec2-user@ec2-54-208-32-170.compute-1.amazonaws.com

8. Create putty file using .pem file

9. Download WinSCP and connect to EC2 instance using .ppk file

10. install Docker Compose v2 correctly on Amazon Linux 2:
=========================================================
i. Create Plugin Directory:
mkdir -p ~/.docker/cli-plugins

ii. Download Docker Compose v2 Binary

curl -SL https://github.com/docker/compose/releases/download/v2.35.1/docker-compose-linux-x86_64 \
-o ~/.docker/cli-plugins/docker-compose

Note:You can replace v2.3 with the latest version if needed.

iii. Make It Executable
chmod +x ~/.docker/cli-plugins/docker-compose

iv. Test It
 docker compose version
=================================================================
sudo systemctl stop docker (stop docker)

sudo systemctl start docker (start docker)

====================================
1. sudo service docker start
2. docker ps -a
3. sudo docker start <contaner id first 3 letters>
4. curl http://localhost:8001
5. docker logs <contaner id first 3 letters>

Rebuild docker compose:
===========================
sudo systemctl stop docker
docker compose build (rebuild docker compose file - goto baxter directory and run)
docker compose up (Execute docker compose)
docker exec <container_id> printenv (Get container details)
docker exec -it [containername] /bin/bash - to get shell

