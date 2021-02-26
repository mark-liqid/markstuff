import time
from .TomcatPower import TomcatPower
from .TomcatClean import TomcatClean
from .tomcatlocation import get_catalina_location
from .tomcatlocation import get_tomcat_location
from utils.message.Message import Message


class TomcatManager(object):
    def __init__(self):
        self._tomcatpower = TomcatPower(get_catalina_location())
        self._tomcatclean = TomcatClean(get_tomcat_location())

    def start(self):
        self._tomcatpower.start()

    def stop(self):
        self._tomcatpower.shut_down()
        self.shut_down_check()

    def shut_down_check(self):

        # check for 20 seconds if tomcat has shut down
        # to prevent following commands from running before
        # tomcat is fully stopped.

        t_end = time.time() + 20
        while time.time() < t_end:
            if self._tomcatpower.is_running():
                continue
            else:
                Message('Tomcat Stopped Successfully')
                self._tomcatclean.clean()
                break
        else:
            Message('Forcing Tomcat to Stop')
            self._tomcatpower.force_shut_down()
            self.shut_down_check()
