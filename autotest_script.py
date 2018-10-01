from random import *
from poly import *
import timeit
from poly_autotest import *


polys_attempted = 0
polys_solved = 0
solve_time = 0

end_time = 60

while True:

    polys_attempted += 1
    print(polys_attempted)

    (output, root_list) = autogen_poly(verbose=False,max_exponent=4, max_order=10)
    t0 = timeit.default_timer()
    try:
        roots = output.find_roots(verbose=False, rel_tol=1E-10)
    except:
        print('Root Solver Error')
        print('Original Poly:', output.coeff_list)
        print('Original Roots:', root_list)
    t1 = timeit.default_timer()

    root_list = sorted(root_list, key=abs)
    roots = sorted(roots, key=abs)

    for i in range(len(root_list)):
        root_list[i] = round_to_sigfigs(root_list[i], sig_figs=7)

    root_list = [abs(x) for x in root_list]
    roots = [abs(x) for x in roots]

    if root_list == roots:
        polys_solved += 1

    solve_time += (t1 - t0)

    if solve_time > end_time:
        break

print('Percent Correctly Solved:', 100.0*polys_solved/polys_attempted, '%')
print('Average Attempt Time:', solve_time/polys_attempted, 'sec')