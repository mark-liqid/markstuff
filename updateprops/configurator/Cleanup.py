import utils.executor as executor


class Cleanup(object):
    def __init__(self, locations):
        self._location = locations

    def clean(self):
        file = self._location + '.bak'
        executor.run(["rm", file])
