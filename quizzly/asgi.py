"""
ASGI config for quizzly project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from . import ProtocolTypeRouter,AuthMiddlewareStack,URLRouter
from django.core.asgi import get_asgi_application
import accounts.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
            URLRouter(accounts.routing.websocket_urlpatterns)
    )  ,
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
})