import configparser

class Config:
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file)

class DatabaseConfig(Config):
    def __init__(self, file):
        super().__init__(file)
        self.data = self.config["database"]
        req = ["host","port","username","password","dbname"]
        for k in req:
            if k not in self.data:
                raise Exception("Missing key: " + k)

db = DatabaseConfig("db.ini")
print("Config loaded successfully")