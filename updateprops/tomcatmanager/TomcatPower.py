import os
import utils.executor as executor
import tomcatmanager.error as error
from utils.message.Message import Message


class TomcatPower(object):
    def __init__(self, path):
        self._directory = path

    def start(self):
        Message('Starting Tomcat')
        os.chdir(self._directory)
        start = executor.run(["./catalina.sh", 'start'])
        if start.returncode != 0:
            raise error.TomcatStartUpError('Problem starting up Tomcat!')
        else:
            Message('Tomcat Started successfully')

    def shut_down(self):
        if self.is_running():
            os.chdir(self._directory)
            stop = executor.run(['./catalina.sh', 'stop'])
            if stop.returncode != 0:
                Message('Cant gracefully stop Tomcat, attempting to kill process.')
                self.force_shut_down()
        else:
            Message('Tomcat is already stopped')

    @staticmethod
    def force_shut_down():
        kill = executor.run(['pkill', '-9', 'java'])
        if kill.responsecode != 0:
            raise error.TomcatShutDownError('Problem shutting down Tomcat!')
        else:
            Message('Tomcat killed successfully.')

    @staticmethod
    def is_running():
        process = os.popen('ps aux | grep java').read()
        if 'tomcat' in process:
            return True
        else:
            return False
