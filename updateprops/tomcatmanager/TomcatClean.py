import os
from utils.message.Message import Message
import utils.executor as executor
import tomcatmanager.error as error


class TomcatClean(object):
    def __init__(self, path):
        self._directory = path

    def clean(self):
        self.clean_dir(self._directory + '/webapps/liqidui')
        self.clean_dir(self._directory + '/temp')
        self.clean_dir(self._directory + '/work/Catalina/localhost/liqidui')
        Message('Tomcat Cleaned')

    def clean_dir(self, location):
        dir = self._directory + location
        if os.path.isdir(dir):
            cmd = executor.run(['rm', '-rf', dir])
            if cmd.responsecode != 0:
                raise error.TomcatCleanDirError('Problem cleaning ' + location)
