class net(object):
    current_net = 0

    def __init__(self, name=None):
        self.name = name
        self.id = net.current_net
        net.current_net += 1

        self.output_port = None
        self.input_port_list = []

    def __str__(self):
        if self.name is None:
            name = ''
        else:
            name = self.name

        string = 'Net named ' + name + ', ID ' + str(self.id) + \
        ', connected to ' + str(self.output_port)

        return string

    def make_connection(self, output_port=None, input_port=None, ):
        
        print('connecting', self.name)
        print('output_port', output_port)
        print('input_port', input_port)
        if output_port is not None:
            if self.output_port is None:
                # if output_port is None, it has never been assigned
                self.output_port = output_port
                output_port.connected_net = self
            else:
                # port already assigned, for now overwrite without asking, but warn
                print('Net ' + self.name + 'was already connected to an output port, it has been overwritten')
                output_port.connected_net.output_port = None
                self.output_port = output_port
                output_port.connected_net = self

        if input_port is not None:
            self.input_port_list.append(input_port)


class node(object):
    current_node = 0

    def __init__(self, name=None):
        self.id = node.current_node
        node.current_node += 1

        self.name = name
        self.output_port_list = []
        self.input_port_list = []
        self._nextport = 0

    def create_in_port(self, alias=None):
        temp_port = port(self._nextport, out_or_in='in', alias=alias, parent=self)
        self.input_port_list.append(temp_port)
        self._nextport += 1

    def create_out_port(self, alias=None):
        temp_port = port(self._nextport, out_or_in='out', alias=alias, parent=self)
        self.output_port_list.append(temp_port)
        self._nextport += 1

    def make_connection(self, net_obj, port_num=0, port_alias=None):
        found_port = False

        if port_alias is not None:
            # Search for port by alias

            for item in self.input_port_list:
                print('searching for', port_alias)
                print('item name', item.alias)
                if item.alias == port_alias:
                    print('match')
                    found_port = True
                    net_obj.make_connection(input_port=item)
                else:
                    print('not match')

            if found_port is False:
                for item in self.output_port_list:
                    if item.alias is port_alias:
                        found_port = True
                        net_obj.make_connection(output_port=item)
        else:
            # Search for port by number

            for item in self.input_port_list:
                if item.num == port_num:
                    found_port = True
                    net_obj.make_connection(input_port=item)

            if found_port is False:
                for item in self.output_port_list:
                    if item.num is port_num:
                        found_port = True
                        net_obj.make_connection(output_port=item)

    # def find_loops_downstream(self):


class port(object):

    def __init__(self, num, out_or_in='out', alias=None, parent=None):
        self.num = num
        self.out_or_in = out_or_in
        self.alias = alias
        self.connected_net = None
        self.parent = parent

    def __str__(self):
        if self.alias is None:
            alias = ''
        else:
            alias = self.alias

        if self.parent is None:
            parent = 'None'
        else:
            parent = self.parent.name

        string = 'node ' + parent + ' ' + self.out_or_in + 'port ' + alias
        return string
