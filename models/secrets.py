from base64 import urlsafe_b64encode
from getpass import getpass
from os import environ, getlogin, getuid, path
from pwd import getpwuid
from uuid import uuid1

from tortoise.models import Model


class Secrets(Model):
    """Looks for the env vars ``USER`` and ``PASSWORD``, requests from the user if unavailable.

    >>> Secrets

    """

    if not environ.get('COMMIT'):
        USERNAME: str = environ.get('USER', path.expanduser('~') or getpwuid(getuid())[0] or getlogin())
        PASSWORD: str = environ.get('PASSWORD')

        if not USERNAME:
            USERNAME: str = input(__prompt='Enter username: ')
            environ['USER'] = USERNAME  # Store as env var so, value remains despite restart

        if not PASSWORD:
            PASSWORD: str = getpass(prompt='Enter PASSWORD: ')
            environ['PASSWORD'] = PASSWORD  # Store as env var so, value remains despite restart
