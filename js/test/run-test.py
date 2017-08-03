# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function, absolute_import

import atexit
import json
import os
from subprocess import Popen
import sys

from tornado import gen
from tornado.ioloop import IOLoop
from notebook.notebookapp import NotebookApp
from traitlets import Bool, Unicode

from ipython_genutils.tempdir import TemporaryDirectory


try:
    from unittest.mock import patch
except ImportError:
    from mock import patch # py3


HERE = os.path.dirname(__file__)


def get_command(nbapp):
    """Get the command to run."""
    # Compatibility with Notebook 4.2.
    token = getattr(nbapp, 'token', '')
    config = dict(baseUrl=nbapp.connection_url, token=token,
                  foo='bar')

    print('\n\nNotebook config:')
    print(json.dumps(config))

    with open(os.path.join(HERE, 'injector.js'), 'w') as fid:
        fid.write("""
        var node = document.createElement('script');
        node.id = 'jupyter-config-data';
        node.type = 'application/json';
        node.textContent = '%s';
        document.body.appendChild(node);
        """ % json.dumps(config))

    return ['karma', 'start'] + sys.argv[1:]


def create_notebook_dir():
    """Create a temporary directory with some file structure."""
    nbdir = TemporaryDirectory()
    os.makedirs(os.path.join(nbdir.name, os.path.join(u'sub ∂ir1', u'sub ∂ir 1a')))
    os.makedirs(os.path.join(nbdir.name, os.path.join(u'sub ∂ir2', u'sub ∂ir 1b')))

    atexit.register(nbdir.cleanup)
    return nbdir.name


def create_env():
    ipydir = TemporaryDirectory()
    config_dir = TemporaryDirectory()
    home = TemporaryDirectory()
    dirs = [ipydir, home, config_dir]
    env = {
        'HOME': home.name,
        'JUPYTER_CONFIG_DIR': config_dir.name,
        'IPYTHONDIR': ipydir.name,
    }
    atexit.register(lambda: [d.cleanup() for d in dirs])
    return env


@gen.coroutine
def run(cmd):
    """Run the cmd and exit with the return code"""
    yield gen.moment  # sync up with the ioloop

    shell = os.name == 'nt'
    proc = Popen(cmd, shell=shell)
    print('\n\nRunning command: "%s"\n\n' % ' '.join(cmd))

    # Poll the process once per second until finished.
    while 1:
        yield gen.sleep(1)
        if proc.poll() is not None:
            break

    exit(proc.returncode)


@gen.coroutine
def exit(code):
    """Safely stop the app and then exit with the given code."""
    yield gen.moment   # sync up with the ioloop
    IOLoop.current().stop()
    sys.exit(code)


class TestApp(NotebookApp):
    """A notebook app that supports a unit test."""

    open_browser = Bool(False)
    notebook_dir = Unicode(create_notebook_dir())
    allow_origin = Unicode('*')

def main():
    """Run the unit test."""
    with patch.dict('os.environ', create_env()):
        app = TestApp()

        if app.version == '4.3.0':
            msg = ('Cannot run unit tests against Notebook 4.3.0.  '
                'Please upgrade to Notebook 4.3.1+')
            print(msg)
            sys.exit(1)

        app.initialize([])  # reserve sys.argv for the command
        cmd = get_command(app)
        run(cmd)

        try:
            app.start()
        except KeyboardInterrupt:
            exit(1)


if __name__ == '__main__':
    main()
