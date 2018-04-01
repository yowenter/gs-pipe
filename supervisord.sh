cat <<EOT > /etc/supervisord.conf

[supervisord]
nodaemon=true

[program:app]
directory=/usr/src/
command=gunicorn -k gevent -w 1 --max-requests 50000 --max-requests-jitter 5000 --access-logfile - --error-logfile - -b 0.0.0.0:5000 gs_pipe.api:app
autorestart=true
startsecs=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0

[program:worker]
command=rq worker 
autorestart=true
startsecs=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0



[program:redis]
command=/usr/bin/redis-server /etc/redis.conf
autorestart=true
startsecs=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0


EOT


exec /usr/bin/supervisord


