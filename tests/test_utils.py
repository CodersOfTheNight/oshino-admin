from oshino_admin.util import parse_plugin


def test_parse_definition():
    plugin_def = 'some_plugin       =>  Desc goes here'
    package, desc = parse_plugin(plugin_def)

    assert package == 'some_plugin'
    assert desc == 'Desc goes here'
