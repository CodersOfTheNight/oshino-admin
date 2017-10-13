import sys

import pip
import click
import requests

from oshino_admin import daemon


@click.group()
def main():
    pass

@main.group('plugin')
def plugin():
    pass


def get_plugins():
    resp = requests.get('https://raw.githubusercontent.com/CodersOfTheNight/'
                        'oshino-admin/master/package_manager/plugins.txt')
    lines = resp.text.split('\n')
    return [plugin.rstrip() for plugin in lines]


def validate_plugin(fn):
    def wrapper(*args, **kwargs):
        plugins = get_plugins()
        package = kwargs['package_name']
        if not package in plugins:
            print("Invalid plugin '{0}'".format(package))
            sys.exit(1)

        return fn(*args, **kwargs)

    return wrapper


@plugin.command('list')
def plugin_list():
    for plugin in get_plugins():
        if plugin in sys.modules.keys():
            print("{0}*".format(plugin))
        else:
            print(plugin)


@plugin.command('install')
@click.argument('package_name')
@validate_plugin
def install(package_name):
    pip.main(['install', package_name, '--upgrade'])


@plugin.command('uninstall')
@click.argument('package_name')
@validate_plugin
def uninstall(package_name):
    pip.main(['uninstall', package_name])


@main.command('status')
@click.option('--pid', help='Pid for process', default='/var/run/oshino.pid')
def status(pid):
    daemon.status(pid)


@main.command('start')
@click.option('--config', help='Config path', default='config.yaml')
@click.option('--pid', help='Pid for process', default='/var/run/oshino.pid')
@click.option('--verbose/--normal', help='Verbose', default=False)
@click.option('--logfile', help='Where to put logs', default=None)
def start(config, pid, verbose, logfile):
    print('Starting...')
    daemon.start_daemon(config, pid, verbose, logfile)


@main.command('stop')
@click.option('--pid', help='Pid for process', default='/var/run/oshino.pid')
def stop(pid):
    print('Stopping...')
    daemon.stop_daemon(pid)



if __name__ == "__main__":
    main()
