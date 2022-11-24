from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/manideep/documents/fastapi/fastapi_app.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/manideep/documents/fastapi/access_log'
errorlog =  '/home/manideep/documents/fastapi/error_log'
