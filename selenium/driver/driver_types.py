class DriverTypes(object):

    @staticmethod
    def getDriverName(name):
        return {
            'ff': 'FIREFOX',
            'firefox':'FIREFOX',
            'chrome': 'CHROME'
        }.get(name)
