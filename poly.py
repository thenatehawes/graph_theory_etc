class poly(object):

    def __init__(self, coeff_list=None, order=None):
        if coeff_list is None:
            coeff_list = [1]

        if order is None:
            order = len(coeff_list)

        self.coeff_list = coeff_list
        self.order = order

    def __mul__(self, other):

        result = [None] * (self.order + other.order)
        for j in range(other.order):
            
