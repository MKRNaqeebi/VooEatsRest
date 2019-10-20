
systemctl stop uwsgi
mkdir -p /etc/uwsgi/sites
cat > /etc/uwsgi/sites/VooEatsRest.ini <<EOL
[uwsgi]
project = VooEatsRest
uid = mkrnaqeebi
base = /home/mkrnaqeebi

for-readline = %(base)/env.txt
  env = %(_)
endfor = 


chdir = %(base)/%(project)
home = %(base)/%(project)/venv
module = VooEatsRest.wsgi:application

master = true
processes = 2
enable-threads = yes
lazy-apps = yes

socket = %(base)/%(project).sock
chown-socket = %(uid):www-data
chmod-socket = 660
vacuum = true
EOL

cat > /etc/systemd/system/uwsgi.service <<EOL
[Unit]
Description=uWSGI Emperor service

[Service]
ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
EOL

# ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled

# nginx -t

# systemctl restart nginx
# systemctl daemon-reload
systemctl start uwsgi


# Configure supervisor to run the node app.
# uwsgi --http 0.0.0.0:8008 --home /home/mkrnaqeebi/VooEatsRest/venv --chdir /home/mkrnaqeebi/VooEatsRest -w VooEatsRest.wsgi
