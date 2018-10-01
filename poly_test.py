from poly import *

p0 = poly([1, 2, 3, 0, 0])
p1 = poly([2, 4, 6, 8])

p2 = p0 + p1

print('p0 order:', p0.order)
print('p1 order:', p1.order)
print('p2 order:', p2.order)
print(p2.coeff_list)

p3 = poly([5, 1])
p4 = poly([-5, 1])

p5 = p3 * p4

print('p5 order:', p5.order)
print(p5.coeff_list)

roots = p5.find_roots()
print(roots)

p6 = poly([10, 1])
p7 = p5 * p6

roots = p7.find_roots()
print(roots)

(nr_root, c_flag, count) = p7.newton_raphson(initial_guess=14 + 1j*10)
print('Newton Raphson Convergence:', c_flag)
print('On Iteration:', count)
print('Root Found:', nr_root)

# l = [2, 1, 1, 1]
# print(l[0:-2])
(m_root, c_flag, count) = p7.muller()
print('Muller Convergence:', c_flag)
print('On Iteration:', count)
print('Root Found:', m_root)

print('Testing Division:')
print('p7 = p5 * (s + 10)')
print('p7 =', p7.coeff_list)
print('p5 =', p5.coeff_list)
(output, remainder) = p7.synthetic_division(p6)
print('p7 / (s + 10) =', output.coeff_list)

p8 = poly([(2 + 1j*20), 1])
p9 = p8 * poly([(2 - 1j*20), 1])
p10 = p7 * p9

p11 = poly([(25 + 1j*30), 1]) * poly([(25 - 1j*30), 1]) * poly([125, 1]) * poly([5, 1])
(output, remainder) = p11.synthetic_division(poly([(25 + 1j*30), 1]))
print('Remainder from imagniary division:', remainder)

result = p10.comp_horner(2 + 3j)
result2 = p10.evaluate(2 + 3j)
print('evaluate result', result2)
print('comp horner result:', result)
# a = -8
# print('a', a**(1/3))

# ptest=p9 * p6
# print('ptest:', ptest.coeff_list)
# # roots = ptest.find_roots()
# roots = cubic_eqn(ptest.coeff_list)
# print(roots)
# print('ptest_eval r1:', ptest.evaluate(roots[0]))

print('')
print('Testing Root Finder on p10')
print('p10:', p10.coeff_list)
roots = p10.find_roots()
print('Roots found:', roots)
