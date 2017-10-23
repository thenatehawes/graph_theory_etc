from node_net import node


class constant_source(node):
    default_num = 0

    def __init__(self, name=None):
        if name is None:
            name = 'constant' + str(constant_source.default_num)
            constant_source.default_num += 1

        node.__init__(self, name=name)
        self.create_out_port(alias='signal out')


class terminator(node):
    default_num = 0

    def __init__(self, name=None):
        if name is None:
            name = 'terminator' + str(integrator.default_num)
            terminator.default_num += 1

        node.__init__(self, name=name)
        self.create_in_port(alias='signal in')


class integrator(node):
    default_num = 0

    def __init__(self, name=None):
        if name is None:
            name = 'integrator' + str(integrator.default_num)
            integrator.default_num += 1

        node.__init__(self, name=name)

        self.create_in_port(alias='signal in')
        self.create_out_port(alias='signal out')


class gain(node):
    default_num = 0

    def __init__(self, name=None):
        if name is None:
            name = 'gain' + str(gain.default_num)
            gain.default_num += 1

        node.__init__(self, name=name)

        self.create_in_port(alias='signal in')
        self.create_out_port(alias='signal out')


class summing_junction(node):
    default_num = 0

    def __init__(self, num_inputs, name=None):
        if name is None:
            name = 'sum' + str(summing_junction.default_num)
            summing_junction.default_num += 1

        node.__init__(self, name=name)

        for i in range(num_inputs):
            string = 'signal in' + str(i)
            self.create_in_port(alias=string)

        self.create_out_port(alias='signal out')


class transfer_function(node):
    default_num = 0

    def __init__(self, name=None, xfer='1'):
        if name is None:
            name = 'xfer' + str(transfer_function.default_num)
            transfer_function.default_num += 1

        node.__init__(self, name=name)

        self.xfer = xfer

        self.create_in_port(alias='signal in')
        self.create_out_port(alias='signal out')
