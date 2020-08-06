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

## Installing RC Application on Docker
