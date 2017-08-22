import sys

import pip
import click

@click.group()
def main():
    pass

def get_plugins():
    with open('package_manager/plugins.txt', 'r') as f:
        return [plugin.rstrip() for plugin in f.readlines()]

def validate_plugin(fn):
    def wrapper(*args, **kwargs):
        plugins = get_plugins()
        package = kwargs['package_name']
        if not package in plugins:
            print("Invalid plugin '{0}'".format(package))
            sys.exit(1)

        return fn(*args, **kwargs)

    return wrapper

@main.command('list')
def plugins():
    for plugin in get_plugins():
        if plugin in sys.modules.keys():
            print("{0}*".format(plugin))
        else:
            print(plugin)

@main.command('install')
@click.argument('package_name')
@validate_plugin
def install(package_name):
    pip.main(['install', package_name, '--upgrade'])


@main.command('uninstall')
@click.argument('package_name')
@validate_plugin
def uninstall(package_name):
    pip.main(['uninstall', package_name])



if __name__ == "__main__":
    main()
