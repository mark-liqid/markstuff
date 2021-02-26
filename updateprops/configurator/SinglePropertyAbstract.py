class SinglePropertyAbstract(object):
    def __init__(self, ui_value, api_value):
        self._ui_value = ui_value
        self._api_value = api_value

    def get_ui_value(self):
        return self._ui_value

    def get_api_value(self):
        return self._api_value
