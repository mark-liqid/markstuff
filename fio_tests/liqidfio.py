import os

original = open("configurable.fio")
fiobuf = original.read()
testfile = open("testrun.fio")

tests = {'1': 'read', '2': 'randread', '3': 'write', '4': 'randwrite', '5': 'randrw', '6': 'rw'}

# Pull in data for fio test configuration


print('What kind of test is being run? \n 1: Seq Read \n 2: Random Read \n 3: Seq Write \n 4: Random Write')
print(' 5: Random Read and Write \n 6: Seq Read and Write\n')
selection = raw_input("Selection : ")

print('You will be running ' + tests[selection])

# finished configuration of what tests to run, now selecting targets.
# using targ% for ease of editing by folks who don't know python
drivecount = raw_input("How many m.2s are being tested?")
if drivecount == 4:
    print('Select the targets for your test.')
    os.system('ls /dev/|grep nvme')
    print("Your targets shouldn't have partitions. ie do not select 'p' drives.")
    print("Example input : /dev/nvme0n1")
    targ1 = raw_input("Target 1")
    targ2 = raw_input("Target 2")
    targ3 = raw_input("Target 3")
    targ4 = raw_input("target 4")
else:
    if drivecount == 8:
        print('Select the targets for your test.')
        os.system('ls /dev/|grep nvme')
        print("Your targets shouldn't have partitions. ie do not select 'p' drives.")
        print("Example input : /dev/nvme0n1")
        targ1 = raw_input("Target 1")
        targ2 = raw_input("Target 2")
        targ3 = raw_input("Target 3")
        targ4 = raw_input("Target 4")
        targ5 = raw_input("Target 5")
        targ6 = raw_input("Target 6")
        targ7 = raw_input("Target 7")
        targ8 = raw_input("Target 8")

blocksize = raw_input('What block size should be used?')

qdepth = raw_input('What queue depth should be used?')

runinput = raw_input("How long should the test run, in minutes?")
runtime = runinput*60

jobs = raw_input("How many threads should be run per target?")

ramp = raw_input("How long should I ramp up the drive?")

for line in open(fiobuf):
    fiobuf.write(line.replace('$BLK', blocksize))
    fiobuf.write(line.replace('$DEPTH',qdepth))
    fiobuf.write(line.replace('$RUNTIME', runtime))
    fiobuf.write(line.replace('$JOBS', jobs))
    fiobuf.write(line.replace('$RAMP', ramp))
    fiobuf.write(line.replace('$TEST',selection))
    fiobuf.write(line.replace('$TARG1',targ1))
    fiobuf.write(line.replace('$TARG2',targ2))
    fiobuf.write(line.replace('TARG3', targ3))
    fiobuf.write(line.replace('TARG4',targ4))

original.close()
fiobuf.write(testfile)
testfile.close()

print('Spinning up FIO now.')
os.system('fio testrun.fio')




