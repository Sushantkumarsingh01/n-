import configparser

class DBPropertyUtil:
    @staticmethod
    def get_properties(filename: str):
        config = configparser.ConfigParser()
        config.read(filename)
        return {
            'url': config['DEFAULT']['db.url'],
            'username': config['DEFAULT']['db.username'],
            'password': config['DEFAULT']['db.password']
        }
