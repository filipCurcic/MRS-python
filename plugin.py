class Plugin:
    def __init__(self, metadata):
        self._metadata = metadata
        

    @property
    def name(self):
        return self._metadata.get("name")
    @name.setter
    def name(self, value):
        self.metadata["name"] = value
    @name.deleter
    def name(self):
        del self._metadata["name"]

    @property
    def description(self):
        return self._metadata.get("description")
    
    @description.setter
    def description(self, value):
        self._metadata["description"] = value 

    @description.deleter
    def description(self):
        del self._metadata["description"]

    @property 
    def symbolic_name(self):
        return self._metadata.get("symbolic_name")

    @symbolic_name.setter
    def symbolic_name(self, value):
        self._metadata["symbolic_name"] = value
    
    @symbolic_name.deleter
    def symbolic_name(self):
        del self._metadata["symbolic_name"]

    @property
    def app_version(self):
        return self._metadata.get("app_version")
    
    @app_version.setter
    def app_version(self, value):
        self._metadata["app_version"] = value
    
    @app_version.deleter
    def app_version(self):
        del self._metadata["app_version"]
    
    @property
    def version(self):
        return self._metadata.get("version")
    
    @version.setter
    def version(self, value):
        self._metadata["version"] = value
    
    @version.deleter
    def version(self):
        del self._metadata["version"]
    
    @property
    def category(self):
        return self._metadata.get("category")
    
    @category.setter
    def category(self, value):
        self._metadata["category"] = value
        
    @category.deleter
    def category(self):
        del self._metadata["category"]

    @property
    def enabled(self):
        return self._metadata.get("enabled")

    @enabled.setter
    def enabled(self, value):
        self._metadata["enabled"] = value
    
    @enabled.deleter
    def enabled(self):
        del self._metadata["enabled"]