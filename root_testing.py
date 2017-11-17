from poly import *

poly1 = poly([(100 + 30j), 1]) * poly([(100 - 30j), 1]) * poly([(2091 + 4039j), 1]) * poly([(2091 - 4039j), 1]) * poly([0, 1]) * poly([0, 1]) * poly([-400, 1])
print('Testing Root Finder on poly1')
print('poly1:', poly1.coeff_list)
roots = poly1.find_roots(verbose=True)
print('Roots found:', roots)
