# Ansible Server Base

An Ansible role that configures a server with a simple base configuration. This role can be used 
as starting point for provisioning a new server.

## Variables

See the ```defaults/main.yml``` for the variables

## Tasks

* add-env-variables.yml - Adds variables to dthe /etc/environment
* change-sshd-config.yml - Harding the sshd config
* configure-sudoers.yml - Configure custom sudoers permissions
* copy-ssh-keys.yml - Copy developer keys to the remote host
* create-deployer-ssh-key.yml - Creates deploy key for an CI system
* create-users.yml - Creates new users

## Server security

These tasks in this role perform a only a some standard security settings. 

## License 

MIT 

Copyright 2018 konek.to (https://konek.to)

