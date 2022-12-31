# 0x1A. Application server.

## Resources
1. [Application server vs web server](https://alx-intranet.hbtn.io/rltoken/B9fOBzIxX_t1289WAuRzJw)
2. [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not1. install Gunicorn using virtualenv, just install everything globally)](https://alx-intranet.hbtn.io/rltoken/kpG6RwmwRJHzRmGUM_ERcA)
3. [Running Gunicorn](https://alx-intranet.hbtn.io/rltoken/2LF1j7xKJGYaUtD1HKgUeQ)
4. [Be careful with the way Flask manages slash in route - strict_slashes](https://alx-intranet.hbtn.io/rltoken/lEg0zpkkDcLtdl3VD4ACRQ)
5. [Upstart documentation](https://alx-intranet.hbtn.io/rltoken/mcEsKqFsjJA3tHAjiMknaw)

## identify process running on a port:
1. sudo lsof -ti:${5000}

## kill process
1. sudo kill -9 $(lsof -ti:${PORT})

## stop agent commands running in background
sudo systemctl stop datadog-agent
sudo systemctl disable datadog-agent

## Nginx Configuration steps
1. [Nginx config.](https://ubiq.co/tech-blog/change-nginx-port-number-ubuntu/)

## Others
1. [identify process running on a particular port](https://remarkablemark.org/blog/2016/06/06/kill-used-port/)

## Gunicorn and Nginx
* Gunicorn is a pure-Python HTTP server for WSGI applications. It allows you to run any Python application concurrently by running multiple Python processes within a single dyno. It is basically an application server

* Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. 