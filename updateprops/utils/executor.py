import subprocess


def run(command, chdir = None):
    try:
        return subprocess.run(command, cwd=chdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    except Exception as e:
        failure = subprocess.CompletedProcess(command, 1000)
        failure.stderr = str(e)
        return failure
