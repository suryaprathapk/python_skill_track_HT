# Getting started with docker

## Installation and initial configuration

### Windows Desktop
Windows installation of docker is pretty much striaghtforward, download the installer exe from this link https://www.docker.com/products/docker-desktop
and follow the regular installation steps just like any other sfotware installation.
The installer will also add docker desktop to your system startup, you can choose to disable that in your task manager.

**Sepcific case for some windows 10 builds**

There seems to be error with docker start up on certain version of windows, it becasue of Hyper-V windows feature being disabled.
There are plenty of stackoverflow answers solving this issue, please try it out if you get into these error while trying out docker on your laptop.

### For Linux Machines
For each linux distro, the installation steps change slightly, but on a whole its simple if you do it via a package manager.
In our case, since we have centos standar issue VMs, the following steps are for centos machines using Yum Package manager.

* Login to terminal (Best practice is to install this via root user and the use docker using sudo command with your user login) 
* As a preliminary check, do a `Yum update` 
* Install *yum-utils* with the command `yum install yum-utils`
* Add docker repository to your machine using the command `sudo yum-config-manager \ --add-repo \ https://download.docker.com/linux/centos/docker-ce.repo`
* To Install latest docker engine , use the command `sudo yum install docker-ce docker-ce-cli containerd.io`
* The above comman installs the latest version, if you wish to install any specific version pass on arguments as shown below
    `sudo yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io`
* To start the docker engine, use `sudo systemctl start docker`
* To verify installation, run `docker run hello-world`, You should see a greeting message from a test docker image


**Advanced steps**
* To enable nightly builds `sudo yum-config-manager --enable docker-ce-nightly`
* To enable test channel   `sudo yum-config-manager --enable docker-ce-test`
* Use `--disable` option to disable the channels created in the above steps

## Pulling images and using containers
* To pull an image from docker hub, you can browse around for official images on hub.docker.com or try this command `docker search <image_name>`
* For our case, we will need an image with centos 7, so we will use `docker pull centos:7`, running just `docker pull centos` will pull the latest image
* Run the command `docker images` to list all the images present on your Linux machine
* To start a container use the command `docker run <image_name>:<tag>`
* To start a container interactively use the command `docker run -it <image>:<tag>`, the argument *-it* indicated to run interactive /bin/bash on the container
* Use the commane `docker ps` to list all the containers that are running.
* If you have already started a container and choose to access it interactively then use `docker exec -it <container_id> /bin/bash`
* Exiting the containers with comman `exit` will just close it and all the changes you have done will be gone, to save changes you will have to commit the container 
* To commit the changes you have made, open another terminal (commit can be done on linux terminal, but not from inside the docker terminal)
    use the command `docker commit -m "<your commit message>" <container id> <name to wish to save with>:<tag you wish to add>
* Some times, you will need to access folder contents on linux machine from inside docker (for cases like logging etc.)
    for such purposes use `docker run -v <path to you linux folder>:<folder inside your docker> -it <container id>:<tag>`
* After deploying application ons the container, you might need to expose them for the outside world to use, in such cases, you will need to bind the machine port to a docker port, to do that run a container with this command `docker run -v <path to you linux folder>:<folder inside your docker> -p <post of machine:<port on docker> -it <container id>:<tag>`  
* All docker containers can talk to each other with no additonal provision or setup provided as long as they are on same host/swarm

## Installing RC Application on Docker

### Install OPENJDK
* List the available java versions on Yum `yum list |grep openjdk` --> choose openjdk 1.8.0 devel 64 bit version
* Instaall openjdk with `yum install <java version you chose>
* JAVA_HOME setup `export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk`
* Adding java bin to path - for session `export PATH=$PATH:$JAVA_HOME/bin`
* Run . .bashrc


### Install Tomcat
* Tomcat is not directly available on yum packages list, so we need to get it from apache's website
* Install wget using `yum install wget` to use it to fetch packages in the next step.
* Navigate to opt folder using `cd opt`
* Create an appserver directory 'mkdir appserver`
* Get the tomcat package using `wget https://downloads.apache.org/tomcat/tomcat-9/v9.0.37/bin/apache-tomcat-9.0.37.tar.gz`
* Unpack the package with `tar -xf apache-tomcat-9.0.37.tar.gz`


### To setup RC Application
* Get the build package either from mnpdbuilds of your own git clone.
* In case of mnpdbuilds, run install.sh file
* Copy the cust folder needed for your deployment
* Check the `/bin/env` settings and then run `bin/startapp.sh` in you installer folder.
* As a good practice, decrease you max RAM allotted from 12 BG to 4 GB in your properties.txt file.
* Deployed application can be used using `http://<linux_host_name>:<port>`
* Any error you encounter from here on can be solved in a similar fashion on how you would handle it on a regular linux VM
