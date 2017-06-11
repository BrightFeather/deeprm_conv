# tidier and simpler launcher without use of command line
import os
os.environ["THEANO_FLAGS"] = "device=cpu,floatX=float32"
import sys
import getopt
import matplotlib
matplotlib.use('Agg')

import parameters
import pg_re
import pg_re_single_core
import pg_su
import slow_down_cdf

pa = parameters.Parameters()
pa.type_exp = "pg_re"
# pa.pg_resume = "data/pg_su_net_file_9990.pkl"
pa.simu_len = 50
pa.num_ex = 10
pa.output_filename= "data/pg_re_conv"
pa.output_freq=2
pg_re_single_core.launch(pa)
