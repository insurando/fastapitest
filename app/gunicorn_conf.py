
import json
import multiprocessing
import os

workers_per_core_str = os.getenv("WORKERS_PER_CORE", "1")
max_workers_str = os.getenv("MAX_WORKERS")
use_max_workers = None
if max_workers_str:
    use_max_workers = int(max_workers_str)
web_concurrency_str = os.getenv("WEB_CONCURRENCY", None)

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "80")
bind_env = os.getenv("BIND", None)
use_loglevel = os.getenv("LOG_LEVEL", "debug")
if bind_env:
    use_bind = bind_env
else:
    use_bind = f"{host}:{port}"

cores = multiprocessing.cpu_count()
workers_per_core = float(workers_per_core_str)
default_web_concurrency = workers_per_core * cores
if web_concurrency_str:
    web_concurrency = int(web_concurrency_str)
    assert web_concurrency > 0
else:
    web_concurrency = max(int(default_web_concurrency), 2)
    if use_max_workers:
        web_concurrency = min(web_concurrency, use_max_workers)
accesslog_var = os.getenv("ACCESS_LOG", "-")
use_accesslog = accesslog_var or None
errorlog_var = os.getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None
graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "120")
timeout_str = os.getenv("TIMEOUT", "120")
keepalive_str = os.getenv("KEEP_ALIVE", "5")

# Gunicorn config variables
loglevel = use_loglevel
workers = web_concurrency
bind = use_bind
errorlog = use_errorlog
worker_tmp_dir = "/dev/shm"
accesslog = use_accesslog
graceful_timeout = int(graceful_timeout_str)
timeout = int(timeout_str)
keepalive = int(keepalive_str)

# logging
#--access-logformat "{'remote_ip':'%(h)s','request_id':'%({X-Request-Id}i)s','response_code':'%(s)s','request_method':'%(m)s','request_path':'%(U)s','request_querystring':'%(q)s','request_timetaken':'%(D)s','response_length':'%(B)s'}"
# "date='%(t)s' ip='%(h)s' method='%(m)s' querystring='%(q)s' status='%(s)s' response_time='%(D)s'"
#access_log_format = os.getenv("ACCESS_LOG_FORMAT") or None
#access_log_format = "%(t)s"
#from gunicorn import glogging    
#glogging.Logger.error_fmt = '{"AppName": "%(name)s", "logLevel": "%(levelname)s", "Timestamp": "%(created)f", "Class_Name":"%(module)s", "Method_name": "%(funcName)s", "process_id":%(process)d, "message": "%(message)s"}'
#glogging.Logger.datefmt = ""
#glogging.Logger.access_fmt = '{"AppName": "%(name)s", "logLevel": "%(levelname)s", "Timestamp": "%(created)f","Class_Name":"%(module)s", "Method_name": "%(funcName)s", "process_id":%(process)d, "message": "%(message)s"}'
#glogging.Logger.syslog_fmt = '{"AppName": "%(name)s", "logLevel": "%(levelname)s", "Timestamp": "%(created)f","Class_Name":"%(module)s", "Method_name": "%(funcName)s", "process_id":%(process)d, "message": "%(message)s"}'


# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "keepalive": keepalive,
    "errorlog": errorlog,
    "accesslog": accesslog,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    "use_max_workers": use_max_workers,
    "host": host,
    "port": port
}
print(json.dumps(log_data))
