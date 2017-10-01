from node_net import node


class constant_source(node):

    def __init__(self, name=None):
        node.__init__(self, name=name)
        self.create_out_port(alias='signal out')


class terminator(node):

    def __init__(self, name=None):
        node.__init__(self, name=name)
        self.create_in_port(alias='signal in')


class integrator(node):

    def __init__(self, name=None):
        node.__init__(self, name=name)

        self.create_in_port(alias='signal in')
        self.create_out_port(alias='signal out')


class gain(node):

    def __init__(self, name=None):
        node.__init__(self, name=name)

        self.create_in_port(alias='signal in')
        self.create_out_port(alias='signal out')


class summing_junction(node):

    def __init__(self, num_inputs, name=None):
        node.__init__(self, name=name)

        for i in range(num_inputs):
            string = 'signal in' + str(i)
            self.create_in_port(alias=string)

        self.create_out_port(alias='signal out')
