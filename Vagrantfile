# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"
    
  #for i in 8000..8010
  #  config.vm.network :forwarded_port, guest: i, host: i
  #end

  config.vm.provider :virtualbox do |v|
    v.name = "devboks"
    v.memory = 1024
    v.cpus = 2
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--ioapic", "on"]
  end

  config.vm.host_name = "devboks"
  #config.vm.network "public_network"
  config.vm.network "private_network", ip: "192.168.33.12"

  config.vm.synced_folder "./", "/workspace/devboks/",  :owner => "vagrant", :group => "vagrant", :mount_options => ['dmode=775', 'fmode=664']
  #config.vm.synced_folder "./src", "/home/vagrant/src",  :owner => "www-data", :group => "www-data", :mount_options => ['dmode=775', 'fmode=664']
  
  config.vm.define :devboks do |devboks|
  end

  # Ansible provisioner.
  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.playbook = "ansible/playbooks/devboks.debian.docker.playbook.yaml"
    ansible.inventory_path = "ansible/inventory/hosts"
    ansible.become = true
  end

end
