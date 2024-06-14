import streamlit as st
from PIL import Image

st.title("Docker Cluster Projects")
image = Image.open('imgs/course_project2.png')
st.image(image, caption='Docker Cluster Setup', use_column_width=True)
st.markdown("""
## Project 1: Docker Cluster Setup

This section provides instructions and screenshots for creating a Docker cluster with 1 master node, 3 worker nodes, and a node for JupyterLab. Worker 3 has exposed port 8083 through the web interface.

### Step-by-Step Instructions

1. **Update and Upgrade the System:**
    ```bash
    sudo apt update
    sudo apt upgrade
    ```
""")

st.markdown("""
2. **Install SSH for Convenience (Optional):**
    ```bash
    sudo apt install openssh-server
    ```
""")
#Set
st.image("imgs/ssh_screenshot.PNG", caption="Install SSH")

st.markdown("""
3. **Install Necessary Dependencies:**
   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-propertiescommon -y
   ```
""")
#Set
st.image("imgs/depen_screenshot.PNG", caption="Install dependencies")

st.markdown("""
         - As the root user add the GPG key for Docker repository.
      ```bash
      sudo su
      ```
      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
      ```         
""")
#Set
st.image("imgs/gpg_key_screenshot.PNG", caption="Add GPG Key")

st.markdown("""
   - Add Docker repository to the list of repositories.
   
   ```bash
   add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
   ``` 
""")
#Set
st.image("imgs/add_repository_screenshot.PNG", caption="Add Repository")

st.markdown("""
4. **Update Repository List:**
    ```bash
    sudo apt update
    ```
""")
#Set
st.image("imgs/update_repositories_screenshot.PNG", caption="Update Repositories")

st.markdown("""
5. **Install Docker and Docker Compose:**
    ```bash
            sudo apt install docker-ce docker-compose -y
    ```
""")
#Set
st.image("imgs/install_docker_screenshot.PNG", caption="Install Docker")

st.markdown("""
6. **Enable and Check Docker Service:**
    ```bash
   sudo systemctl start docker
   
    ```
""")
#Set
st.image("imgs/docker_start_screenshot.PNG", caption="Docker Service")

st.markdown("""
            ```bash
    sudo systemctl status docker
    ```
""")
#Set
st.image("imgs/docker_status_screenshot.PNG", caption="Docker Service Status")

st.markdown("""
7. **Run "Hello World" to Verify Installation:**
    ```bash
    sudo docker run hello-world
    ```
""")
#Set
st.image("imgs/hello_world_screenshot.PNG", caption="Hello World")

st.markdown("""
8. **Create Cluster Directory and Download Dockerfiles:**
            (These files may no longer be available)
    ```bash
    mkdir cluster
   ```
   ```bash
    cd cluster
   ```
   ```bash
    wget https://raw.githubusercontent.com/tnavarrete-iedib/bigdata-23-24/main/docker/spark-master.Dockerfile
   ```
   ```bash
    wget https://raw.githubusercontent.com/tnavarrete-iedib/bigdata-23-24/main/docker/spark-worker.Dockerfile
   ```
   ```bash
    wget https://raw.githubusercontent.com/tnavarrete-iedib/bigdata-23-24/main/docker/jupyterlab.Dockerfile
    ```
            
   - (Shown only the download of the first file for simplicity)
""")
#Set
st.image("imgs/cluster_directory_screenshot.PNG", caption="Cluster Directory")


st.markdown("""
9. **Download and Execute Build Script:**
            (This file may no longer be available)
    ```bash
    wget https://raw.githubusercontent.com/tnavarrete-iedib/bigdata-23-24/main/docker/build.sh
    ```
   ```bash
   sudo bash build.sh
    ```
""")
#Set
st.image("imgs/build_script_screenshot.PNG", caption="Build Script")
st.image("imgs/run_script_screenshot.PNG", caption="Run Script")


st.markdown("""
10. **Verify Image Creation:**
   ```bash
   sudo docker images
   ```
""")
#Set
st.image("imgs/verify_images_screenshot.PNG", caption="Verify Images")


st.markdown("""
11. **Download Docker Compose Configuration:**
            (This file may no longer be available)
    ```bash
    wget https://raw.githubusercontent.com/tnavarrete-iedib/bigdata-23-24/main/docker/docker-compose.yml
    ```
""")
#Set
st.image("imgs/docker_compose_config_screenshot.PNG", caption="Docker Compose Config")

# st.markdown("""
# 11. **Download Docker Compose Configuration:**
#             -(This file may no longer be available)
#     ```bash
#     wget https://raw.githubusercontent.com/tnavarrete-iedib/bigdata-23-24/main/docker/docker-compose.yml
#     ```
# """)

# st.image("imgs/docker_compose_config_screenshot.PNG", caption="Docker Compose Config")

st.markdown("""
12. **Modify docker-compose.yml to Expose Port 8083 for Worker 3:**
""")
#Set
st.image("imgs/expose_port_screenshot.PNG", caption="Expose Port 8083")

st.markdown("""
13. **Start Docker Containers: (From the cluster directory)**
    ```bash
    sudo docker-compose up
    ```
""")
#Set
st.image("imgs/start_containers_screenshot.PNG", caption="Start Containers")

st.markdown("""
14. **Web Interfaces:**
    - **Master Node:**
""")

st.image("imgs/master_node_interface_screenshot.PNG", caption="Master Node")

st.markdown("""
- **Worker 1:**
""")

st.image("imgs/worker1_interface_screenshot.PNG", caption="Worker 1")

st.markdown("""
- **Worker 2:**
""")

st.image("imgs/worker2_interface_screenshot.PNG", caption="Worker 2")

st.markdown("""
- **Worker 3 (Port 8083):**
""")

st.image("imgs/worker3_interface_screenshot.PNG", caption="Worker 3")

st.markdown("""
- **JupyterLab:**
""")

st.image("imgs/jupyterlab_interface_screenshot.PNG", caption="JupyterLab")