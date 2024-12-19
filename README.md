# Geog213-Final
This repository contains the Jupyter Notebook Report for my GEOG213 Final Project, which is on calculating the dNBR of the Butte County Dixie Fire 


## Requirements

You need to have Docker installed on your machine. 


## Instructions

It's recommended to pull the Docker image from Dockerhub. Otherwise, if you prefer, you can build your own image using the instructions in the following section. 

```
docker pull abphill2004/geog213-final:latest
```

```
docker run -it -p 8888:8888 abphill2004/geog213-final:latest
```

- Copy the Jupyter Lab url and paste it in your browser. 
- Open `geog213_phillips_report.ipynb`and `utils.py`to see the code


Build the Docker image:

**Windows users:** It is highly recommended that you pull the Docker image, there seems to be an issue with conda-forge on WSL. 

```
docker build -t geog213-final .
```

Run the container as following after switching to the repository's directory locally:
```
docker run -it -p 8888:8888 geog213-final
```

- Copy the Jupyter Lab url and paste it in your browser. 
- Open `geog213_phillips_report.ipynb`and `utils.py`to see the code
