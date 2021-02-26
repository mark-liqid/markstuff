from .WarLocator import WarLocator
from .WarCompress import WarCompress
from .WarMover import WarMover
from tomcatmanager.tomcatlocation import get_tomcat_location


class WarManager(object):
    def __init__(self, args):
        try:
            war = args.index('-war') + 1
            self.setup(get_tomcat_location(), args[war])
        except ValueError:
            self.setup(get_tomcat_location())

    def setup(self, tomcat_dir, war_location=None):
        self._warlocation = WarLocator()

        if not war_location:
            self._warlocation.collect_input()
        else:
            self._warlocation.set_orig_war_dir(war_location)

        self._warcompress = WarCompress(self._warlocation.get_dirs())

        self._warmover = WarMover(self._warlocation.get_dirs(), self._warcompress.get_war_name(), tomcat_dir)

        self._dirs = self._warlocation.get_dirs()

    def step_one(self):
        self._warmover.move_to_temp()
        self._warcompress.expand()

    def step_two(self):
        self._warcompress.compress()
        self._warcompress.cleanup()
        self._warmover.move_to_tomcat()

    def get_dirs(self):
        return self._dirs
