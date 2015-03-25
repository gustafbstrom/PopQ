#!/usr/bin/env python

import os
import signal
import time
import random
import tempfile

data = [
# CPU
	("What is the Sandy Bridge L1 cache size? (kB)","32"),
	("What is the Sandy Bridge L2 cache size? (kB)","256"),
	("What is the Ivy Bridge L1 cache size? (kB)","64"),
	("What is the Ivy Bridge L2 cache size? (kB)","256"),
	("What size L2 cache have all non-Atom Intel CPUs had sice the introduction of Nehalem 2008? (kB)", "256"),
	("What size is the IL1 and DL1 cache in Intel CPUs since Core 2? (kB)", "32 32"),
	("What is the per-core L2 cache of the Xeon Phi? (kB)", "512"),
# Tilera
	("What is the maximum power consumption of the TILEpro64 (W)","22"),
# Memory
	("What is the default page size in x86_64 systems? (kB)","4"),
	("What is the huge page size in x86_64 systems? (MB)","8"),
	("What is the default page size in sparc systems? (kB)","8"),
# GPU
	("What is the size of the register file in Fermi? (kB)","128"),
	("What is the size of the register file in Kepler? (kB)","256"),
	("What is the Fp Core/(LD/ST) ratio in Kepler","6"),
	("What is the architecture name of the first Mali GPU (T604) to support OpenCL (1.1)?","Midgard"),
	("What is the cache protocol for shared caches between ARM CPUs and GPUs?","snooping"),
	("What is the average power budget of an embedded GPU? (mw)", "850"),
#intercon
	("What is the bandwidth of InfiniBand QDR 1X? (Gbps)","8"),
#language
	("What is NaN!=NaN?","true"),
	("If p is NULL and using lazy-evaluation, does this segfault? if(p!=NULL && p->data > 0)","no")
]

def ctrl_c_handler( signum, frame):
    print "HERE"

signal.signal( signal.SIGALRM, ctrl_c_handler )

fname = tempfile.gettempdir() + "/popresource.txt"

try:
	time.ctime(os.path.getmtime(fname))
	exit(0)
except OSError as e:
	with file(fname, 'a'):
		os.utime(fname, None)
		print "Tempfile stored in %s" % fname

lasttime = time.ctime(os.path.getmtime(fname))
print "last modified: %s" % lasttime
correct = 10

checklist = []

for x in range(0,10):
    try:
	rand_num = int(random.uniform(0,len(data)))
	
	while rand_num in checklist:
		rand_num = int(random.uniform(0, len(data)))

	checklist.append( rand_num )

	randq = data[rand_num]
	print randq[0]
	ans = raw_input("> ")
	if ans != randq[1]:
		print "The answer is: %s" % randq[1]
		correct -= 1
    except KeyboardInterrupt:
        os.system("clear")
        exit(1)
    except EOFError:
        os.system("clear")
        exit(1)


os.system("clear")
print "Score: %1.2f %d/10" % (correct/10.*100., correct)
