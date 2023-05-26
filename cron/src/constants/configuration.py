import os


class Setting:
    def __init__(self):
        self.props = {}

    def __getattr__(self, name):
        return self.props[name]

    def __setattr__(self, name, value):
        if name == "props":
            object.__setattr__(self, name, value)
        else:
            self.props[name] = value
        return 


def get_config_setting():
    setting = Setting()
    setting.notify_token = os.getenv("NOTIFY_TOKEN")
    setting.test_mode = True if os.getenv("TEST_MODE").upper() == "TRUE" else False

    return setting
    