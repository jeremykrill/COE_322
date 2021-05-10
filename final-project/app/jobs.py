# jobs.py
import uuid
from hotqueue import HotQueue
from redis import StrictRedis
import os

redis_ip = os.environ.get('REDIS_IP')

# Create redis routes to manage different functions 
rd = StrictRedis(host=redis_uip, port=6379, db=0)
j =  StrictRedis(host=redis_uip, port=6379, db=1)
q = HotQueue("queue", host=redis_ip, port=6379, db=2)
plot = StrictRedis(host=redis_ip, port=6379, db=3)

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    return 'job.{}'.format(jid)

def _instantiate_job(jid, status, stocks, dates):
    if type(jid) == str:
        return {'jid': jid,
                'status': status,
                'stocks': stocks,
                'dates': dates
        }
    return {'jid': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'stocks': stocks.decode('utf-8'),
            'dates': dates.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    """Save a job object in the Redis jobs database."""
    j.hmset(job_key, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)

def add_job(stocks, dates, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, stocks, dates)
    _save_job(_generate_job_key(jid), job_dict)
    _queue_job(jid)
    return job_dict

def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `new_status`."""
    j.hset(_generate_job_key(jid), 'status', new_status)

def get_job_data(jid):
    """Returns dictionary containing job data"""
    return j.hgetall(_generate_job_key(jid))

def add_image(jid, img):
    """ Adds a job for an image to redis queue"""
    j.hset(_generate_job_key(jid), 'image_status', 'done')
    plot.hset(jid, 'image', img)

