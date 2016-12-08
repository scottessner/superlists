## Required packages:

* Nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host Config

* see nginx.template.conf
* replace SITENAME with domain name, eg staging.my-domain.com

## Systemd Job

* see gunicorn-systemd.template.service
* replace SITENAME with domain name, eg staging.my-domain.com

## Folder structure
Assume we have a user account at /home/username

/home/username
┗━━ sites
    ┗━━ SITENAME
        ┗━━ database
        ┗━━ source
        ┗━━ static
        ┗━━ virtualenv
