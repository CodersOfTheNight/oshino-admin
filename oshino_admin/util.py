import re

PLUGIN_PATT = re.compile(r'(?P<plugin_name>(\w+))\s*=>\s*(?P<plugin_desc>(.*))')

def parse_plugin(plugin_definition):
    result = PLUGIN_PATT.match(plugin_definition)
    return result.group('plugin_name'), result.group('plugin_desc')
