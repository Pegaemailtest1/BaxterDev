===========================================
1. Install Docker desktop for windows
==========================================
    https://www.docker.com/products/docker-desktop/ 
        Select Downloads for windows AMD64 option to dowload docker desktop .exe file

=========================================== 
2. Application folder structure as follows:
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
3. Open downloaded source code in visual studio editor and navigate to BaxterDev folder and run the below commands in terminal
    Install docker compose
        pip install docker-compose
==============================

4. Add environment variable

        Add it to your system PATH
        Check if it's installed:
        Look in:
        C:\Program Files\Docker\Docker\resources\bin
        You should see a docker-compose.exe.

        Add that folder to your system PATH:

        Press Windows Key → Search Environment Variables

        Click Edit the system environment variables

        In the System Properties window, click Environment Variables

        Under System Variables, select Path → click Edit

        Click New, and add:
        C:\Program Files\Docker\Docker\resources\bin
        Click OK and restart VS Code

        Reopen your terminal and run:
        docker-compose version
========================================
4. Run It All
    docker-compose up --build
=========================================

======================================
Install Ollama models:     
======================================
Test Ollama is Running:
        http://ollama:11434/

    Install models into ollama server:
        Embedding MOdel:
            docker exec -it ollama ollama pull mxbai-embed-large
        Foundation Model RAG Based search:
            docker exec -it ollama ollama pull llama3

=================================
