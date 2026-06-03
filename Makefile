PYTHON ?= python3
PELICAN ?= $(PYTHON) -m pelican
PELICANOPTS =

BASEDIR = $(CURDIR)
INPUTDIR = $(BASEDIR)/content
OUTPUTDIR = $(BASEDIR)/output
CONFFILE = $(BASEDIR)/pelicanconf.py
PUBLISHCONF = $(BASEDIR)/publishconf.py

FTP_HOST = localhost
FTP_USER = anonymous
FTP_TARGET_DIR = /

SSH_HOST = localhost
SSH_PORT = 22
SSH_USER = root
SSH_TARGET_DIR = /var/www

S3_BUCKET = pelican

CLOUDFILES_USERNAME = anonymous
CLOUDFILES_API_KEY = dummy
CLOUDFILES_CONTAINER = pelican

DROPBOX_DIR = /Pelican/sites/example

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:PORT'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (visible on the local net)  '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make devserver-global               regenerate and serve on 0.0.0.0    '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync     '
	@echo '   make dropbox_upload                 upload the web site via Dropbox    '
	@echo '   make ftp_upload                     upload the web site via FTP        '
	@echo '   make s3_upload                      upload the web site to S3          '
	@echo '   make cf_upload                      upload the web site to Cloud Files '
	@echo '   make github                         upload the web site to gh-pages    '
	@echo '   git init; make serve                Initialize git repo and serve      '
	@echo '                                                                       '

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver-global:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

github:
	"$(PELICAN)" -s "$(PUBLISHCONF)" $(PELICANOPTS)
	ghp-import -m "Generate Pelican site" -b $(BRANCH) "$(OUTPUTDIR)"
	git push origin $(BRANCH)

.PHONY: html clean regenerate serve serve-global devserver devserver-global publish github
