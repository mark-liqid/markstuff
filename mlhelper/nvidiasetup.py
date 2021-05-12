import os
import sys

blacklist = 'echo "blacklist nouveau" > /etc/modprobe.d/blacklist.conf'

euid = os.geteuid()
if euid != 0:
    print("Not run as root, requesting elevation...")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    os.execlpe('sudo', *args)
    pass

print('Starting Liqid, Inc NVIDIA TF Benchmark Setup....')
os.system('apt update && apt install build-essential -y')

nouveau_status = os.system('lsmod |grep nouveau')

if nouveau_status == "nouveau":
    print('Nouveau is not blacklisted, blacklisting. You will need to reboot.')
    os.system(blacklist)
else:
    if nouveau_status == " ":
        pass

print('Starting NVIDIA driver installation...')

os.system("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin")
os.system('mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600')
os.system('apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub')
os.system('add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"')
os.system('apt update && apt install nvidia-cuda-toolkit -y')


print('Finished NVIDIA Driver and CUDA Toolkit, starting Docker-CE installation')


os.system('apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
os.system('add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
os.system('apt update && apt install docker-ce docker-ce-cli containerd.io -y')


print('Docker.ce Installed, now installing NVIDIA Docker 2')


os.system('curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | apt-key add -')
os.system("curl -s -L https://nvidia.github.io/nvidia-docker/ubuntu20.04/nvidia-docker.list > /etc/apt/sources.list.d/nvidia-docker.list)
os.system('apt update && apt install nvidia-docker2 -y')
os.system('pkill -SIGHUP dockerd')


print('Starting NVIDIA TF Container Download....')
os.system('docker pull nvcr.io/nvidia/tensorflow:20.12-tf2-py3')

print('Complete, to run the container : sudo docker run --gpus all -it --rm -v nvcr.io/nvidia/tensorflow:20.12-tf2-py3')
print('Creating runcontainer.sh with that command....')
os.system('echo sudo docker run --gpus all -it --rm nvcr.io/nvidia/tensorflow:20.12-tf2-py3 > runcontainer.sh')
