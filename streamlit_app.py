import streamlit as st
from PIL import Image

# Set the title of the page
st.title("Docker Cluster Setup")

# Add a description of the task
st.markdown("""
## Section 1: Docker Cluster Setup

This section provides instructions and screenshots for creating a Docker cluster with 1 master node, 3 worker nodes, and a node for JupyterLab. Worker 3 has exposed port 8083 through the web interface.

### Steps Included:
1. **Create a Docker Cluster** with 1 master node and 3 worker nodes.
2. **Set Up a JupyterLab Node** in the cluster.
3. **Expose Port 8083** on Worker 3 for web interface access.
""")

# Display the image of the Docker cluster setup
image = Image.open('imgs/course_project2.png')
st.image(image, caption='Docker Cluster Setup', use_column_width=True)

# Add detailed instructions
st.markdown("""
### Detailed Instructions:

1. **Set Up Docker Environment:**
   - Install Docker on your local machine.
   - Pull the necessary Docker images for the master and worker nodes.

2. **Create Master Node:**
   - Run a Docker container for the master node.
   - Configure the master node settings as per the instructions.

3. **Create Worker Nodes:**
   - Run Docker containers for three worker nodes.
   - Configure each worker node to connect to the master node.

4. **Set Up JupyterLab Node:**
   - Run a Docker container for JupyterLab.
   - Ensure JupyterLab is accessible within the cluster network.

5. **Expose Port 8083 on Worker 3:**
   - Use Docker commands to expose port 8083 on Worker 3.
   - Verify that the port is accessible from the web interface.

### Screenshots:

Below there's a PDF with basic instructions and screenshots showing the process of me setting up the cluster.
            
            (Work in progress)
""")

# You can add more images or screenshots as needed
# st.image('path_to_screenshot_1.png', caption='Step 1: Description')
# st.image('path_to_screenshot_2.png', caption='Step 2: Description')

