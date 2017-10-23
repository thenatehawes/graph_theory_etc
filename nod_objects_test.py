################################################################
# node_objects_test.py
# N.B. Hawes
# 2017 - 09 - 23
#
# Test script for node_objects. Implements a simple driven
# LR circuit.
################################################################
from node_objects import *
from node_net import net

source = constant_source('Source Voltage')
sumjunc = summing_junction(2)
inverseinductance = gain('1/L')
resistance = gain('R')
integration1 = integrator()
termination = terminator('End')

v_s = net('v_s')
v_r = net('v_r')
v_L = net('v_L')
flux = net('flux')
i_L = net('i_L')

print(v_s)

connection_option = True

if connection_option is True:
    source.make_connection(v_s, port_alias='signal out')
    sumjunc.make_connection(v_s, port_alias='signal in0')
    sumjunc.make_connection(v_r, port_alias='signal in1')
    sumjunc.make_connection(v_L, port_alias='signal out')
    integration1.make_connection(v_L, port_alias='signal in')
    integration1.make_connection(flux, port_alias='signal out')
    inverseinductance.make_connection(flux, port_alias='signal in')
    inverseinductance.make_connection(i_L, port_alias='signal out')
    termination.make_connection(i_L, port_alias='signal in')
    resistance.make_connection(i_L, port_alias='signal in')
    resistance.make_connection(v_r, port_alias='signal out')

else:
    v_s.make_connection(output_port=source.output_port_list[0])
    v_s.make_connection(input_port=sumjunc.input_port_list[0])
    v_r.make_connection(input_port=sumjunc.input_port_list[1])
    v_L.make_connection(output_port=sumjunc.output_port_list[0])
    v_L.make_connection(input_port=integration1.input_port_list[0])
    flux.make_connection(output_port=integration1.output_port_list[0])
    flux.make_connection(input_port=inverseinductance.input_port_list[0])
    i_L.make_connection(output_port=inverseinductance.output_port_list[0])
    i_L.make_connection(input_port=termination.input_port_list[0])
    i_L.make_connection(input_port=resistance.input_port_list[0])
    v_r.make_connection(output_port=resistance.output_port_list[0])

print(v_s)

loop = source.find_loops_downstream()

print(loop)