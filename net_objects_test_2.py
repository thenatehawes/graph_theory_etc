################################################################
# node_objects_test_2.py
# N.B. Hawes
# 2017 - 10 - 21
#
# Test script for node_objects. Implements a LCL filter.
# 
################################################################
from node_objects import *
from node_net import net

# Make nodes

source = constant_source('Source Voltage')
output_source = constant_source('Output Source Voltage')

LR1_xfer = transfer_function('LR1', '1/(L1*s + R1)')
C_xfer = transfer_function('C', '1/s/C')
LR2_xfer = transfer_function('LR2', '1/(L2*s + R2')

sumjunc_1 = summing_junction(2)
sumjunc_2 = summing_junction(2)
sumjunc_3 = summing_junction(2)

termination = terminator('End')

# Make nets
v_s = net('v_s')
v_lr1 = net('v_lr1')
i_1 = net('i_1')
i_c = net('i_c')
v_c = net('v_c')
v_out = net('v_out')
v_lr2 = net('v_lr2')
i_2 = net('i_2')

# Link up nodes/nets
source.make_connection(v_s, port_alias='signal out')

sumjunc_1.make_connection(v_s, port_alias='signal in0')
sumjunc_1.make_connection(v_c, port_alias='signal in1')
sumjunc_1.make_connection(v_lr1, port_alias='signal out')

LR1_xfer.make_connection(v_lr1, port_alias='signal in')
LR1_xfer.make_connection(i_1, port_alias='signal out')

sumjunc_2.make_connection(i_1, port_alias='signal in0')
sumjunc_2.make_connection(i_2, port_alias='signal in1')
sumjunc_2.make_connection(i_c, port_alias='signal out')

C_xfer.make_connection(i_c, port_alias='signal in')
C_xfer.make_connection(v_c, port_alias='signal out')

sumjunc_3.make_connection(v_c, port_alias='signal in0')
sumjunc_3.make_connection(v_out, port_alias='signal in1')
sumjunc_3.make_connection(v_lr2, port_alias='signal out')

output_source.make_connection(v_out, port_alias='signal out')

LR2_xfer.make_connection(v_lr2, port_alias='signal in')
LR2_xfer.make_connection(i_2, port_alias='signal out')

termination.make_connection(i_2, port_alias='signal in')

loops = source.find_loops_downstream()
paths = source.find_paths(termination)

loops_touch = loops[0].touch_check(loops[1])
print('Loop touch check is', loops_touch)
print(loops[0])

myarray = numpy.array([1,2,3])
print(myarray)
