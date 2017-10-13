from daemonize import Daemonize

from oshino.run import main

DEFAULT_PID = '/var/run/oshino'


def start_daemon(config_path, pid=DEFAULT_PID):
    def wrapped():
        return main(("--config", config_path, ))

    daemon = Daemonize(app='oshino', pid=pid, action=wrapped)
    daemon.start()
    return daemon
