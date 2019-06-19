# dependencies
sudo apt-add-repository universe
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install 			\
	build-essential 			\
	libssl-dev 					\
	libffi-dev 					\
	python3-dev 				\
	python3-pip  				\
	git 						\
	curl						\
	apt-transport-https 		\
	ca-certificates 			\
	software-properties-common 	-q -y

#install apache
#sudo apt-get install 			\
#	apache2 					\
#	apache2-dev					\
#	libapache2-mod-wsgi-py3	-q -y
#pip3 install mod_wsgi


#install pyodbc
#sudo apt-get install 			\
#	unixodbc-dev 				\
#	unixodbc-bin -q -y               
#sudo pip3 install pyodbc

# install ansible
sudo apt-get install ansible -y
#install pip packages
pip3 install requests
pip3 install django
pip3 install djangorestframework
sudo pip3 install virtualenv
pip3 install statsd

#install docker on Ubuntu
if [ "$(lsb_release -is)" == "Ubuntu" ] ; then
	echo "---------INSTALLING DOCKER ON UBUNTU--------------"
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	sudo apt-key fingerprint 0EBFCD88
	sudo add-apt-repository \
	"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	$(lsb_release -cs) \
	stable"
	sudo apt update
	apt-cache policy docker-ce
	yes | sudo apt install docker-ce
	#check that docker is installed successfully	
	#sudo systemctl status docker
	sudo docker run hello-world   
	sudo pip3 install docker-compose
#install docker on Raspbian	
elif [ "$(lsb_release -is)" == "Raspbian" ]; then
#installing docker on raspberry-pi 
	echo "---------INSTALLING DOCKER ON RASPBIAN--------------"
	sudo apt-get install \
	     apt-transport-https \
	     ca-certificates \
	     curl \
	     gnupg2 \
	     software-properties-common
	curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
	sudo apt-key fingerprint 0EBFCD88
	echo "deb [arch=armhf] https://download.docker.com/linux/debian \
	     $(lsb_release -cs) stable" | \
	    sudo tee /etc/apt/sources.list.d/docker.list
	sudo apt-get install docker-ce 
	sudo docker run armhf/hello-world
	docker-compose --version
####raspberry-pi##########
fi


#install nodejs
yes | curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install -y build-essential
sudo npm install npm --global

 ###docker on ubuntu### 
