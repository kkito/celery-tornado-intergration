from celery import Celery
import contextvars
from kombu.common import oid_from

task_list = [
    'celery_app.tasks'
]

class MyCelery(Celery):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context_oid = contextvars.ContextVar('context_oid')
        self.context_backend = contextvars.ContextVar('context_backend')
        
    @property
    def thread_oid(self):
        """Per-thread unique identifier for this app."""
        return self.context_oid.get(oid_from(self, threads=True))

    @property
    def backend(self):
        """Current backend instance."""
        return self.context_backend.get(self._get_backend())

celery_app = MyCelery("testTornadoCelery")
# celery_app = Celery("testTornadoCelery")
celery_app.config_from_object('celery_app.config')
celery_app.autodiscover_tasks(task_list)