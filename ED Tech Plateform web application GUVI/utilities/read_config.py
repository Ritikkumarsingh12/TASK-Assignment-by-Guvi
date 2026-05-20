from configparser import ConfigParser

config = ConfigParser()
config.read("config/config.ini")

class ReadConfig:

    @staticmethod
    def get_application_url():
        return config.get('common info', 'baseURL')

    @staticmethod
    def get_email():
        return config.get('common info', 'email')

    @staticmethod
    def get_password():
        return config.get('common info', 'password')

    @staticmethod
    def get_browser():
        return config.get('common info', 'browser')
