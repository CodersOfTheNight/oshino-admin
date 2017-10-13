import os

from daemonize import Daemonize
from logbook import Logger, FileHandler, DEBUG, INFO

from oshino.config import load
from oshino.core.heart import start_loop

DEFAULT_PID = '/var/run/oshino'


def start_daemon(config_path, pid=DEFAULT_PID, verbose=False, logfile=None):
    logger = Logger('oshino')
    keep_fds = []
    if logfile:
        level = DEBUG if verbose else INFO
        fh = FileHandler(logfile, level=level)
        logger.handlers.append(fh)
        fh.push_application()
        keep_fds.append(fh.stream.fileno())

    def wrapped():
        cfg = load(config_path)
        return start_loop(cfg)

    daemon = Daemonize(
            app='oshino',
            pid=pid,
            action=wrapped,
            verbose=verbose,
            keep_fds=keep_fds,
            logger=logger,
            chdir=os.getcwd()
    )
    daemon.start()
    return daemon

def stop_daemon(pid=DEFAULT_PID):
    with open(pid, 'r') as f:
        os.kill(int(f.read()), 0)

def status(pid=DEFAULT_PID):
    if os.path.exists(pid):
        with open(pid, 'r') as f:
            print('Process is running on: {0}'.format(f.read()))
    else:
        print('Process is not running')
