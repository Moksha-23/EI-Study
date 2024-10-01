class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance.configuration = {}
        return cls._instance

    def set_configuration(self, key, value):
        self.configuration[key] = value

    def get_configuration(self, key):
        return self.configuration.get(key)

config1 = ConfigurationManager()
config1.set_configuration("database", "localhost")

config2 = ConfigurationManager()
print(config2.get_configuration("database"))  
print(config1 is config2)  
