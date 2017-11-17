from cmath import *


class poly(object):

    def __init__(self, coeff_list=None):
        if coeff_list is None:
            coeff_list = [1]
            order = 0
        else:
            last_non_zero = 0

            for i in range(len(coeff_list)):
                item = coeff_list[-i - 1]

                if ((item > 0 or item < 0)):
                    last_non_zero = -i - 1
                    break

            order = len(coeff_list) + last_non_zero

        self.coeff_list = coeff_list
        self.order = order

    def __add__(self, other):
        temp_list = add_lists(self.coeff_list, other.coeff_list)

        result = poly(coeff_list=temp_list)
        return result

    def __mul__(self, other):
        temp_list = [0] * (self.order + other.order + 1)

        for j in range(other.order + 1):
            temp = mult_list_by_constant(shift_list_right(self.coeff_list, j), other.coeff_list[j])
            temp_list = add_lists(temp_list, temp)

        result = poly(coeff_list=temp_list)
        return result

    def derivative(self):

        result_list = [0] * (self.order)

        for i in range(self.order):
            result_list[i] = (i + 1) * self.coeff_list[i+1]

        result = poly(result_list)

        return result

    def evaluate(self, x):

        output = 0

        for i in range(self.order + 1):
            output += ((self.coeff_list[i]) * (x**i))

        return output

    def find_roots(self, rel_tol=1E-7, sig_figs=7, verbose=False):
        root_list = []
        poly_obj = self

        while True:

            if (poly_obj.order == 1):
                if verbose:
                    print('Analytic 1st order solution')
                root_list.append(poly_obj.coeff_list[0])
                break

            elif (poly_obj.order == 2):
                # Direct solve w/ quadratic equation
                if verbose:
                    print('Analytic 2nd order solution')
                output_list = quadratic_eqn(poly_obj.coeff_list)
                root_list.append(output_list[0])
                root_list.append(output_list[1])
                break

            # elif (poly_obj.order == 3): # cube root problem!!!!
            #     # Direct solve w/ cubic equation
            #     if verbose:
            #        print('Analytic 3rd order solution')
            #     print(poly_obj.coeff_list)
            #     output_list = cubic_eqn(poly_obj.coeff_list)
            #     print(output_list)
            #     root_list.append(output_list[0])
            #     root_list.append(output_list[1])
            #     root_list.append(output_list[2])
            #     break

            # elif (poly_obj.order == 4):
            # Quartic eqn has a problem, i'll fix it later
            # Direct solve w/ cubic equation
                # output_list = quartic_eqn(poly_obj.coeff_list)
                # root_list.append(output_list[0])
                # root_list.append(output_list[1])
                # root_list.append(output_list[2])
                # root_list.append(output_list[3])
            else:
                # Order is > 5, Find a root (or a complex pair)
                if verbose:
                    print('Starting Muller Coarse Solver')
                (root, cflag, n) = poly_obj.muller(initial_guess=(0 + 1j, 1 + 1j, 2+1j), tol=1E0, verbose=verbose)
                if verbose:
                    print('Starting NR Solver w/ initial point', root)
                (root, cflag, n) = poly_obj.newton_raphson(initial_guess=root, tol=rel_tol, verbose=verbose)
                
                if verbose:
                    print('Root found', root)
                root_list.append(root)
                if (abs(root.imag) > 1E-6*abs(root.real)):
                    if verbose:
                        print('Assuming complex pair found:', root.conjugate())
                    root_list.append(root.conjugate())

                    found_root = poly([-root, 1])

                    if verbose:
                        print('Deflating Polynomial')
                    (deflated_poly, remainder) = poly_obj.synthetic_division(found_root)
                    if verbose:
                        print('Remainder 1:', remainder)
                    found_root = poly([-root.conjugate(), 1])
                    (deflated_poly, remainder) = deflated_poly.synthetic_division(found_root)
                    if verbose:
                        print('Remainder 2:', remainder)
                else: 
                    found_root = poly([-root, 1])               
                    if verbose:
                        print('Deflating Polynomial')
                    (deflated_poly, remainder) = poly_obj.synthetic_division(found_root)
                    if verbose:
                        print('Remainder 1:', remainder)

                if verbose:
                    print('Deflated Poly:', deflated_poly.coeff_list)
                if len(root_list) == self.order:
                    break
                else:
                    poly_obj = deflated_poly

        for i in range(len(root_list)):
            root_list[i] = round_to_sigfigs(root_list[i], sig_figs)

        return root_list


    def newton_raphson(self, initial_guess=0, tol=1E-6, max_iter=50, verbose=False):

        poly_derivative = self.derivative()

        value = [initial_guess] * (max_iter + 1)

        if verbose:
            print('nr iter 0 :', value[0])
        count = 0

        while True:
            count += 1

            delta_value = self.evaluate(value[count - 1]) / poly_derivative.evaluate(value[count - 1])
            value[count] = value[count - 1] - delta_value

            if verbose:
                print('nr iter', count, ':', value[count], ':', delta_value)

            if (abs(delta_value) < tol):
                cflag = True
                break
            elif (count == max_iter):
                cflag = False
                break

        return (value[count], cflag, count)

    def muller(self, initial_guess=(0, 1, 2), tol=1E-1, max_iter=50, verbose=False):

        value = [0] * (max_iter + 4)

        value[0] = initial_guess[0]
        value[1] = initial_guess[1]
        value[2] = initial_guess[2]

        cflag = False

        count = 2

        if verbose:
            print('m iter 0-2:', value[0:2])

        while True:
            count += 1

            w = self.divided_diff([value[count-1], value[count-2]])
            w += self.divided_diff([value[count-1], value[count-3]])
            w -= self.divided_diff([value[count-2], value[count-3]])

            disc = sqrt(w**2 - 4*self.evaluate(value[count - 1])*self.divided_diff([value[count-1], value[count-2], value[count-3]]))

            w_plus_disc = w + disc
            w_minus_disc = w - disc

            divisor = max(abs(w_plus_disc), abs(w_minus_disc))

            delta_value = 2*self.evaluate(value[count - 1]) / divisor

            value[count] = value[count - 1] - delta_value

            if verbose:
                print('m iter', count, ':', value[count], ':', delta_value)

            if (abs(delta_value) < tol):
                cflag = True
                break
            elif (count == max_iter):
                break
     
        return (value[count], cflag, count)


    def divided_diff(self, input_list):

        # print('divided_diff input_list:', input_list)

        if (len(input_list) == 1):
            # print('divided_diff evaluate')
            diff = self.evaluate(input_list[0])
        else:
            left_list = input_list[0:len(input_list)-1]
            # print('left_list:', left_list)
            right_list = input_list[1:len(input_list)]
            # print('right_list:', right_list)

            diff = (self.divided_diff(left_list) - self.divided_diff(right_list)) / (input_list[0] - input_list[-1])

        return diff

    def synthetic_division(self, other):
        if (other.order != 1):
            return

        divisor = -other.coeff_list[0]
        # print('divisor:', divisor)

        output_list = [0] * (self.order + 1)
        output_list[-1] = self.coeff_list[-1]

        for i in range(len(output_list)-2, 0, -1):
            # print('self.coeff_list[i+1]', self.coeff_list[i+1])
            output_list[i] = output_list[i+1] * divisor + self.coeff_list[i]
            # print('i:', i, 'output_list:', output_list)

        remainder = output_list[0]
        poly_list = output_list[1:len(output_list)]

        output = poly(poly_list)
        return (output, remainder)

def add_lists(list_1, list_2):

    len_1 = len(list_1)
    len_2 = len(list_2)
    max_len = max(len_1, len_2)
    min_len = min(len_1, len_2)

    result = [0] * max_len
    for i in range(min_len):
        result[i] = list_1[i] + list_2[i]

    if (min_len != max_len):
        if (len_1 == max_len):
            result[min_len:max_len] = list_1[min_len:max_len]
        else:
            result[min_len:max_len] = list_2[min_len:max_len]

    return result


def mult_list_by_constant(list_in, constant):
    result = [0] * len(list_in)

    for i in range(len(list_in)):
        result[i] = constant * list_in[i]

    return result


def shift_list_right(list_in, shift_amount):
    result = [0] * (len(list_in) + shift_amount)

    for i in range(len(list_in)):
        result[-i - 1] = list_in[-i - 1]

    return result


def round_to_sigfigs(x, sig_figs=6):

    string = '{0:.' + str(sig_figs) + '}'
    realpart = float(string.format(x.real))
    imagpart = float(string.format(x.imag))

    if (imagpart == 0.0):
        return realpart
    else:
        return complex(realpart, imagpart)


def quadratic_eqn(input_list):
    a = input_list[2]
    b = input_list[1]
    c = input_list[0]

    disc = sqrt(b**2 - 4*a*c) / (2*a)
    output_list = []
    output_list.append(-b/(2*a) + disc)
    output_list.append(-b/(2*a) - disc)

    return output_list


def cubic_eqn(input_list):
    a2 = input_list[2] / input_list[3]
    a1 = input_list[1] / input_list[3]
    a0 = input_list[0] / input_list[3]

    Q = (3*a1 - a2**2)/9
    R = (9*a2*a1 - 27*a0 - 2*a2**3)/54

    D = Q**3 + R**2
    S = cube_root(R + sqrt(D))
    T = cube_root(R - sqrt(D))

    # -math.pow(3, float(1)/3)

    r1 = S + T - a2/3
    r2 = -0.5*(S + T) + 0.5*1j*sqrt(3)*(S-T) - a2/3
    r3 = -0.5*(S + T) - 0.5*1j*sqrt(3)*(S-T) - a2/3

    output_list = []
    output_list.append(r1)
    output_list.append(r2)
    output_list.append(r3)

    return output_list

# def cube_root(x):
#     if (x.imag > 0):
#         print(x)
#     if x >= 0:
#         return x**(1/3)
#     elif x < 0:
#         return -(abs(x)**(1/3))

        # elif (self.order == 4):
        #     # Direct solve w/ quartic equation
        #     b = self.coeff_list[3] / self.coeff_list[4]
        #     c = self.coeff_list[2] / self.coeff_list[4]
        #     d = self.coeff_list[1] / self.coeff_list[4]
        #     e = self.coeff_list[0] / self.coeff_list[4]



        #     order3_poly = poly([d, c, b, a])
        #     order3_roots = order3_poly.find_roots()

        #     for i in range(3):
        #         if (order3_roots[i].imag == 0):
        #             print('root selected', i)
        #             real_root = order3_roots[i]
        #             if (i == 1):
        #                 break

        #     R = sqrt(0.25*p**2 - q + real_root)
        #     print('R is:', R)
        #     quartic_tol = 1E-8
        #     if (abs(R) < quartic_tol):
        #         print('R zero')
        #         D = sqrt(0.75*p**2 - 2*q + 2*sqrt(real_root**2 - 4*s))
        #         E = sqrt(0.75*p**2 - 2*q - 2*sqrt(real_root**2 - 4*s))
        #     else:
        #         print('R non-zero')
        #         D = sqrt(0.75*p**2 - R**2 - 2*q + 0.25*(4*p*q - 8*r - p**3)/R)
        #         E = sqrt(0.75*p**2 - R**2 - 2*q - 0.25*(4*p*q - 8*r - p**3)/R)

        #     r1 = -p/4 + 0.5*(R + D)
        #     r2 = -p/4 + 0.5*(R - D)
        #     r3 = -p/4 - 0.5*(R + E)
        #     r4 = -p/4 - 0.5*(R - E)

        #     root_list.append(r1)
        #     root_list.append(r2)
        #     root_list.append(r3)
        #     root_list.append(r4)
        # else:
        #     print('not implemented')
        #     