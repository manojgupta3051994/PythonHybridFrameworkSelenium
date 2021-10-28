import configparser


config = configparser.RawConfigParser()
config.read(r'C:\Users\Manoj\Desktop\Python - Selenium Practice\HDD\env\Configurations\config.ini')


class ReadProp:

    @staticmethod
    def readURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def readUsername():
        url = config.get('common info','username')
        return url

    @staticmethod
    def readPassword():
        url = config.get('common info','password')
        return url






