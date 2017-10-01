from node_net import node, net

node1 = node()
node1.create_out_port(alias='hi')


print(node1.id)
print(node.current_node)
print(node1.output_port_list)