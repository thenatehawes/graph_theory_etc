from random import *
from poly import *
import timeit
import pickle
import os

double_limit = 0.05  # Chance of double root
triple_limit = 0.001  # Chance of triple root
imag_limit = 0.15  # 1 - Chance of real root

root_tolerance = 0.001 # How close is close enough for a "true" result
N = 300 # How many polynomials to check


def autogen_poly(max_order=15, max_exponent=5, min_exponent=-3, verbose=False):

    rand_order = random() * max_order
    first = True
    root_list = []

    if verbose:
        print('Poly Auto-Gen')
        print('Poly Order:', rand_order)

    while True:

        # check for double/triple root
        double_check = random()
        triple_check = random()

        if double_check < double_limit:
            num_roots = 2
            if verbose:
                print('Double Root')
        elif triple_check < triple_limit:
            num_roots = 3
            if verbose:
                print('Triple Root')
        else:
            num_roots = 1
            if verbose:
                print('Single Root')

        # real part
        significand = random() * 9.999999 * 2 - 9.999999
        exponent = random() * (max_exponent - min_exponent) + min_exponent
        realpart = significand * 10**exponent

        imag_check = random()
        if imag_check > imag_limit:
            # imag part
            significand = random() * 9.999999 * 2 - 9.999999
            exponent = random() * (max_exponent - min_exponent) + min_exponent
            imagpart = significand * 10**exponent
        else:
            imagpart = 0

        if verbose:
            print('Root Generated:', realpart + 1j*imagpart)

        if abs(imagpart) > 0:
            temp_poly = poly([realpart + 1j*imagpart, 1]) * poly([realpart - 1j*imagpart, 1])
        else:
            temp_poly = poly([realpart + 0j, 1])

        if verbose:
            print('Temp Poly:', temp_poly.coeff_list)

        temp_poly2 = poly([1])
        for i in range(num_roots):
            if verbose:
                print('Temp Poly2:', temp_poly2.coeff_list)

            temp_poly2 = temp_poly * temp_poly2
            root_list.append(-realpart - 1j*imagpart)
            if abs(imagpart) > 0:
                root_list.append(-realpart + 1j*imagpart)

        if verbose:
            print('Temp Poly2:', temp_poly2.coeff_list)

        if first:
            out_poly = temp_poly2
            first = False
        else:
            out_poly = out_poly * temp_poly2

        if verbose:
            print('Out Poly:', out_poly.coeff_list)

        if out_poly.order > rand_order:
            break

    return (out_poly, root_list)

failed = 0
failed_list = []
failed_roots = []
for i in range(N):
    print('Polynomial', i, ':')

    t0 = timeit.default_timer()
    (output, root_list) = autogen_poly(verbose=False)
    t1 = timeit.default_timer()
    roots = output.find_roots(verbose=False)
    t2 = timeit.default_timer()

    root_list = sorted(root_list, key=abs)
    roots = sorted(roots, key=abs)

    for i in range(len(root_list)):
        root_list[i] = round_to_sigfigs(root_list[i], sig_figs=7)

    root_list_abs = [abs(x) for x in root_list]
    roots_abs = [abs(x) for x in roots]

    roots_equal = [abs(x-y)/abs(y) < root_tolerance for x,y in zip(root_list_abs, roots_abs)]

    print('Result')
    print('Poly Order', output.order)
    print('Autogen roots are equal to found roots:', all(roots_equal))
    # print('Autogen time:', t1 - t0)
    print('Solve time:', t2 - t1)
    print('')

    if not all(roots_equal):
        print('autogen poly roots:',root_list)
        print('found roots:',roots)
        failed += 1
        failed_list.append(output)
        failed_roots.append(root_list)

print('')
print('Overall Solve Success:', str(100*(N-failed)/N))

# Load old failed_list if it exists
if os.path.exists('failed.pkl'):
    f = open('failed.pkl', 'rb')
    old_poly, old_roots = pickle.load(f)
    old_poly = old_poly + failed_list
    old_roots = old_roots + failed_roots
    failed = [old_poly, old_roots]
    f.close()
    os.remove('failed.pkl')
else:
    failed = [failed_list, failed_roots]

f = open('failed.pkl', 'wb')
pickle.dump(failed, f)
