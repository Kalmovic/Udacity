# Project Item Catalog - Udacity
### Full Stack Web Development ND
_______________________
## About

This project has the objective of configuring a server in AWS services, having in mind security, and uploading a project online.

- Server: 3.80.85.4
- SSH port: 2200
- URL: http://3.80.85.4

# Steps

### Obtaining Ubuntu Linux Server instance on Amazon Lightsail
- Create AWS account
- Select `Create an instance`
- Select `Linux/Unix`
- Select OS Only and Ubuntu as blueprint
- Select a plan (the minimun is enought, and it is possible to cancel it later before being charged)
- Give you instance a name
- `Create`

### Create SSH Key Lightsail
- CLick on `Account`
- Select `SSH Keys`
- Download private key from the SSH keys section in the Account section on Amazon Lightsail. The file name should be like LightsailDefaultPrivateKey-us-east-2.pem
- Create a new file named lightsail_key.rsa under ~/.ssh folder on your local machine
- Copy and paste content from downloaded private key file to lightsail_key.rsa
- connect
- update and upgrade inside server

### Change door SSH de 22 to 2200
- Run $ sudo nano /etc/ssh/sshd_config to open up the configuration file
- Change the port number from 22 to 2200 in this file
- Save and exit the file
- Restart SSH: $ sudo service ssh restart

### Configure the Uncomplicated Firewall (UFW) to allow only incoming calls to SSH (porta 2200), HTTP (porta 80) e NTP (porta 123).
- sudo ufw status (inativo)
- sudo ufw default deny incoming
- sudo ufw default allow outgoing
- sudo ufw allow 2200/tcp
- sudo ufw allow www
- sudo ufw allow 123/udp
- sudo ufw deny 22
- sudo ufw enable
- sudo ufw status (ativo)
- change in the Networking area server Delete default SSH port 22 and add port 80, 123, 2200

### Adding User Grader && SSH Key
- sudo adduser grader
- Create a file named grader under this path: $ sudo touch /etc/sudoers.d/grader
- Edit this file: $ sudo nano /etc/sudoers.d/grader, add code grader ALL=(ALL:ALL) ALL. Save and exit
- create ssh-keygen in local machine
    - save file in ~/.ssh/
    - grab its content: cat ~/.ssh/FILE-NAME.pub
- these steps in the server:
    - mkdir /home/grader/.ssh
    - touch .ssh/authorized_keys
    - nano .ssh/authorized_keys
        - Copy the content from the file created before.
    - chmod 700 /home/grader/.ssh
    - chmod 644 /home/grader/.ssh/authorized_keys
    - chown grader:grader /home/grader/.ssh
    - disable passwd login for grader: sudo nano /etc/ssh/sshd_config

### Changing timezone to UTC
- sudo dpkg-reconfigure tzdata
- select none
- select UTC

### Installing Apache

- sudo apt-get install apache2
- http://3.80.85.4/ will open Apache2 Ubuntu Default Page

### Installing mod-wsgi
- sudo apt-get install libapache2-mod-wsgi python-dev
- Por fim, reinicie o Apache com o comando sudo apache2ctl restart.
- check python is ok with `python`

### Install Postgre SQL
- sudo apt-get install postgresql
- check if PostgreSQL does not allow remote connections [here](https://www.postgresql.org/docs/9.1/auth-pg-hba-conf.html)

### Create PostgreSQL user 'catalog'
- Switch to PostgreSQL defualt user postgres: $ sudo su - postgres
- Connect to PostgreSQL: $ psql
- Create user catalog with LOGIN role: # CREATE ROLE catalog WITH PASSWORD 'passwd';
- Allow user to create database tables: # ALTER USER catalog CREATEDB;
- Create database: # CREATE DATABASE catalog WITH OWNER catalog;
- Connect to database catalog: # \c catalog
- Revoke all the rights: # REVOKE ALL ON SCHEMA public FROM public;
- Grant access to catalog: # GRANT ALL ON SCHEMA public TO catalog;
- Exit psql: \q 10.Exit user postgres: exit

### Install git
[Helpful link](https://davidegan.me/hide-git-repos-on-public-sites/)
- sudo apt-get install git
- Prevent .git
    - `sudo nano .htaccess`
    - Add these lines: 
```
# ==================================================================
# Prevent .git access
# ==================================================================
RedirectMatch 404 /\.git
```

### Clone application from github
- Create dictionary: `mkdir /var/www/catalog`
- CD to this directory: `cd /var/www/catalog`
- Clone the catalog app: `sudo git clone 'URL' catalog`

### Install dependencies...
- Run these comands:
    - `sudo apt-get install python-pip` to get pip
    - `sudo pip install -r requirements.txt` (file in the repo)
    - `sudo pip install --upgrade pip` (recommended)

### Setup virtual host
- `sudo touch /etc/apache2/sites-available/catalog.conf`
- Helpul links:
- [How to configure Apache](https://www.digitalocean.com/community/tutorials/como-configurar-apache-virtual-hosts-no-ubuntu-14-04-lts-pt)
- [Deploy mod_wsgi](http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/)
- Run:
    - `sudo a2ensite catalog` to enable the virtual host
    - `sudo service apache2 restart` to restart apache
    - `sudo service apache2 reload` to reload apache

### Configure .wsgi file
- `sudo touch /var/www/catalog/catalog.wsgi`
- These lines added:
```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/catalog/')
from catalog import app as application
application.secret_key = 'super_secret_key'
```

# Inspiration:

[otsop110](https://github.com/otsop110/fullstack-nanodegree-linux-server-configuration)