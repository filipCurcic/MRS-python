from plugin import Plugin
from plugin_manager import PluginManager
m1 = {"name": "nPlugin","description": "Description","symbolic_name":"P1","app_version":"1.0.0","version":"v1.1","category":"Tools","metadata":False}
p1 = Plugin(m1)
p2 = Plugin(m1)
p3 = Plugin(m1)
p4 = Plugin(m1)
p5 = Plugin(m1)

plugins = [p1, p2, p3, p4, p5]
pm = PluginManager(plugins)

pm.printPlugins()





