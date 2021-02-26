from utils.message.Message import Message


class WarLocator(object):
    def __init__(self):
        self._orig_war_dir = None
        self._temp_war_dir = '/tmp'

    def collect_input(self):
        while True:
            warinput = input("Location of new .war file? ")
            if not warinput:
                Message('Invalid or empty input ')
                continue
            else:
                self.set_orig_war_dir(warinput)
                break

    def set_orig_war_dir(self, loc):
        self._orig_war_dir = loc

    def get_orig_war_dir(self):
        return self._orig_war_dir

    def get_temp_war_dir(self):
        return self._temp_war_dir

    def get_dirs(self):
        return [self._orig_war_dir, self._temp_war_dir]
