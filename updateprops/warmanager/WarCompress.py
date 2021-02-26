import os
import utils.executor as executor
import warmanager.error as error
from utils.message.Message import Message


class WarCompress(object):
    def __init__(self, location):
        self._locations = location
        self._war_name = self.compute_war_name()
        pass

    def compute_war_name(self):
        name = self._locations[0].split('/')
        return name[len(name) - 1]

    def get_war_name(self):
        return self._war_name

    def expand(self):
        Message('Expanding .war file')
        cmd = executor.run(
            ['unzip', '-q', self._locations[1] + "/" + self._war_name, '-d', self._locations[1] + '/unziptemp'])
        if cmd.returncode != 0:
            raise error.WarExpandError('Problem unzipping the .war file!')

    def compress(self):
        Message('Compressing .war file')
        args = ['zip', '-r', '/tmp/' + self._war_name, '*']
        cmd = executor.run(args, '/tmp/unziptemp')
        if cmd.returncode != 0:
            print(cmd)
            raise error.WarCompressError('Problem compressing the .war file!')

    def cleanup(self):
        Message('Cleaning up temp files')
        os.chdir('/tmp')
        cmd = executor.run(['rm', '-rf', self._locations[1] + '/unziptemp'], '/tmp')
        if cmd.returncode != 0:
            raise error.WarCleanupError('Problem cleaning up temp files!')
