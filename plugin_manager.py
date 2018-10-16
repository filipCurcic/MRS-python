class PluginManager:
    def __init__(self):
        self._plugins = []

    def install(plugin_path):
        #otvara fajl, stavlja metadata u _plugins
        #jedan metadata, jedan plugin
        return True

    def uninstall(plugin_symbolic_name):
        return True

    def enable(self, plugin_symbolic_name):
        for i in self._plugins:
            if i.symbolic_name == plugin_symbolic_name:
                i.enabled = True
                return True

        
    def disable(self, plugin_symbolic_name):
        for i in self._plugins:
            if i.symbolic_name == plugin_symbolic_name:
                i.enabled = False
                return True
                

    @property
    def enabled_plugins(self):
        return filter(lambda x: x.enabled, self._plugins)
    
    @property
    def disabled_plugins(self):
        return filter(lambda x: not x.enabled, self._plugins)

    @property
    def plugins(self):
        return self._plugins

    def printPlugins(self):
        for i in self._plugins:
            print(i)
    

