oshino-admin
=============
Administration module for Oshino.
Should come bundled together with Oshino itself.

Managing Plugins
=================
`oshino-admin plugin list` - lists all available plugins

`oshino-admin plugin install <plugin_name>` - installs requested plugin

`oshino-admin plugin uninstall <plugin_name>` - uninstalls requested plugin

Managing Oshino
===============

`oshino-admin start --config=config.yaml --pid=oshino.pid` 

`oshino-admin status --pid=oshino.pid` 

`oshino-admin stop --pid=oshino.pid` 

Be aware, that default PID path `/var/run/oshino.pid` might be unaccessible by oshino-admin (Lacking of root permissions).
Custom pid path can be defined (as show in example above). Main problem is that you need to direct into correct PID for each service command.

Generating Config
==================
`oshino-admin config init <config_name>.yml`
