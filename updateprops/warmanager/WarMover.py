import utils.executor as executor
import warmanager.error as error
from utils.message.Message import Message


class WarMover(object):
    def __init__(self, war_location, war_name, tomcat_location):
        self._war_locations = war_location
        self._war_name = war_name
        self._tomcat_location = tomcat_location

    def move_to_temp(self):
        Message('Moving .war file to /tmp')
        if self._war_locations[0] != self._war_locations[1] + '/' + self._war_name:
            cmd = executor.run(['mv', self._war_locations[0], self._war_locations[1]])
            if cmd.returncode != 0:
                raise error.WarMoverError('Problem moving .war file to /tmp')
        else:
            Message('.war file already in /tmp')

    def move_to_tomcat(self):
        Message('Moving new .war file to tomcat directory')
        cmd = executor.run(['mv', self._war_locations[1] + '/' + self._war_name, self._tomcat_location + '/webapps'])
        if cmd.returncode != 0:
            raise error.WarMoverError('Problem moving .war file to Tomcat')
