from fastapi import FastAPI, Request
import logging
from logstash_async.handler import AsynchronousLogstashHandler

app = FastAPI()
ELASTIC_HOST = "logstash"
ELASTIC_TCP_PORT = 50000 # must be the same as in /etc/logstash/conf.d/input.conf

logger = logging.getLogger(f"app_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler('/tmp/app.log')
logstash_handler = AsynchronousLogstashHandler(ELASTIC_HOST, ELASTIC_TCP_PORT, database_path=None)

file_handler.setFormatter(formatter)
logstash_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(logstash_handler)

@app.get("/greet")
async def greet(name: str, request: Request):
    client_ip = request.client.host
    logger.info(f"Greet {name} for {client_ip}")
    return {"greeting": f"Hello {name}"}
