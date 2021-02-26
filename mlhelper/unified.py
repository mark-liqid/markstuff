import os
import sys

#get you some r00t
euid = os.geteuid()
if euid != 0:
    print("Checking for root..")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    os.execlpe('sudo', *args)
    pass

print('This will install the needed software and libraries for CUDA or ROCM along with Docker and relative containers.')

print("What do you want to install? CUDA and NVIDIA Drivers or ROCM? Or both?")
install_type=raw_input('Nvidia= 1 ROCM= 2 Both=3 ')

print('Checking for docker...')
dockercheck=str(os.system('docker -v'))

if 'Docker' in dockercheck == False:
    print('Installing Docker.ce...')
    os.system('apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y')
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
    os.system('add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
    os.system('apt update && apt install docker-ce docker-ce-cli containerd.io -y')
    print('Docker installed.. continuing with installation...')
else : pass

#If the user wants CUDA or both...
if install_type==1 or 3:
    print('Installing NVIDIA CUDA and NVIDIA Docker2')
    #check for nouveau and blacklist it
    print('Checking for Nouveau blacklist and blacklisting if not already...')
    if os.path.lexists('/etc/modprob.d/blacklist.conf') == False :
        print('Nouveau is not blacklisted, I can blacklist it for you. If it is already blacklisted skip.')
        cont=str(raw_input ('Continue? y/n '))
        if cont=="y":
            blacklist = 'echo "blacklist nouveau" | tee /etc/modprobe.d/blacklistnoveau.conf'
            print('Nouveau is not blacklisted at /etc/modprobe.d/blacklistnoveau.conf')
            print('Please restart and rerun the script.')
            sys.exit(0)
        elif cont=="n":
            print('Would you like to continue or quit?')
            cont=str(raw_input("Type quit to quit or hit enter to continue "))
            if 'q' in cont:
                print('Exiting')
                sys.exit(0)
            else:pass
    else : pass
    print('This Nouveau was already blacklisted by this script, continuing.')
    print('Starting NVIDIA benchmarking setup.')
    os.system("wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin")
    os.system('mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600')
    os.system('apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub')
    os.system('add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /"')
    os.system('apt update && apt install cuda -y')
    os.system('curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - distribution=$(. /etc/os-release;echo $ID$VERSION_ID)')
    os.system("curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list |  tee /etc/apt/sources.list.d/nvidia-docker.list")
    os.system('apt update && apt install nvidia-docker2 -y')
    os.system('pkill -SIGHUP dockerd')
    print('Now pulling the TF Docker from NGC')
    os.system('docker pull nvcr.io/nvidia/tensorflow:20.12-tf2-py3')
    print('Now downloading the tf_cnn_benchmark from Github')
    os.system('wget https://github.com/tensorflow/benchmarks/archive/master.zip')
    os.system('unzip master.zip')
    print('Complete, to run the container : sudo docker run --gpus all -it --rm -v benchmarks-master/:/workspace nvcr.io/nvidia/tensorflow:20.12-tf2-py3')
    print("You will find an example command line for the NVIDIA container in a file that's been created called nvidiatf")
    os.system("echo python tf_cnn_benchmarks.py --data_format=NCHW --batch_size=256 --num_batches=100 --model=resnet50 --optimizer=momentum --variable_update=replicated --all_reduce_spec=nccl --nodistortions --gradient_repacking=2 --datasets_use_prefetch=True --per_gpu_thread_count=2 --loss_type_to_report=base_loss --compute_lr_on_cpu=True --single_l2_loss_op=True --xla_compile=True --local_parameter_device=gpu --num_gpus=1 --display_every=10 | tee nvidiatf")


#ROCM...
if install_type== 2 or 3:
    print('Installing ROCM DKMS and pulling newest ROCM container for TF....')
    os.system('apt update')

    print('Installing docker.ce...')

    os.system('apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y')
    os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
    os.system(
        'add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
    os.system('apt update && apt install docker-ce docker-ce-cli containerd.io -y')

    print('Starting ROCM installation..')

    os.system('wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -')
    os.system("echo 'deb [arch=amd64] https://repo.radeon.com/rocm/apt/debian/ xenial main' | tee /etc/apt/sources.list.d/rocm.list")
    os.system('apt update && apt install rocm-dkms')

    print('ROCM DKMS installed. Double checking that ML libraries were installed...')

    os.system('sudo apt install rocm-libs miopen-hip rccl -y')

    print('Setting permissions...')
    os.system('usermod -a -G render $LOGNAME')

    print('Pulling latest ROCM TF container...')
    os.system(' docker pull rocm/tensorflow')

    os.system("echo alias drun='sudo docker run -it --network=host --device=/dev/kfd --device=/dev/dri --ipc=host --shm-size 16G --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v $HOME/dockerx:/dockerx' > rocmlaunch")
    print('A file has been created called rocmlaunch, copy and paste this command into your terminal, then run drun rocm/tensorflow:latest')


if install_type==3:
    print("You will find an example command line for the NVIDIA container in a file that's been created called nvidiatf")
    os.system("echo python tf_cnn_benchmarks.py --data_format=NCHW --batch_size=256 --num_batches=100 --model=resnet50 --optimizer=momentum --variable_update=replicated --all_reduce_spec=nccl --nodistortions --gradient_repacking=2 --datasets_use_prefetch=True --per_gpu_thread_count=2 --loss_type_to_report=base_loss --compute_lr_on_cpu=True --single_l2_loss_op=True --xla_compile=True --local_parameter_device=gpu --num_gpus=1 --display_every=10 | tee nvidiatf")


