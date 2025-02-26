from gevent import monkey


monkey.patch_all()


import os  # noqa: E402

from django.core.wsgi import get_wsgi_application  # noqa: E402


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()
