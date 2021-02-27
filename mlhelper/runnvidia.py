import subprocess
import os
import sys

print('This will run the tf_cnn_benchmark script in the nvidia docker.')
batch_size = int(raw_input('Batch size? '))
num_gpu = int(raw_input('Number of GPUs? '))

iterations = int(raw_input('How many iterations do you want to run? '))
logging = str(raw_input('Do you want to log this run? y/n '))
fp = str(raw_input('Do you want to run fp32? Default is fp16. y/d '))

if fp == 'y':
    fp = str('fp16')
elif fp =='n':
    fp = str('fp32')
#requesting root for docker run
euid = os.geteuid()
if euid != 0:
    print("Not run as root, requesting elevation...")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    os.execlpe('sudo', *args)
    pass
#command below is dogshit, need to fix.
#subprocess.Popen("docker run --runtime=nvidia --rm nvcr.io/nvidia/tensorflow:20.12-tf2-py3 python /benchmarks_master/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py --data_format=NCHW --batch_size=",batch_size," --num_batches=",iterations," --model=resnet50 --optimizer=momentum --variable_update=replicated --all_reduce_spec=nccl --nodistortions --gradient_repacking=2 --datasets_use_prefetch=True --per_gpu_thread_count=2 --loss_type_to_report=base_loss --compute_lr_on_cpu=True --single_l2_loss_op=True --xla_compile=True --local_parameter_device=gpu --num_gpus=",num_gpu," --display_every=10")
