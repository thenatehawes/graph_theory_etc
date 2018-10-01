from poly import *
import pickle
import timeit



root_tolerance = 0.001

with open('failed.pkl', 'rb') as f:
    a = pickle.load(f)
    failed_list = a[0]
    failed_roots = a[1]

print('length:', len(failed_list))
print('failed_list')
print(failed_list)
print('')
print('failed_roots')
print(failed_roots)

# for item in failed_list:
item = failed_list[0]
t0 = timeit.default_timer()
roots = item.find_roots(verbose=True, max_iter=500)
t1 = timeit.default_timer()

failed_roots[0] = sorted(failed_roots[0], key=abs)
roots = sorted(roots, key=abs)

print('roots:', sorted(failed_roots[0], key=abs))
print('found:', sorted(roots, key=abs))

root_list_abs = [abs(x) for x in failed_roots[0]]
roots_abs = [abs(x) for x in roots]
rel_err = [abs(x - y)/abs(y) for x,y in zip(root_list_abs, roots_abs)]

roots_equal = [abs(x-y)/abs(y) < root_tolerance for x,y in zip(root_list_abs, roots_abs)]
print('rootsequal', roots_equal)

print('Result')
print('Poly Order', item.order)
print('Autogen roots are equal to found roots:', all(roots_equal))
print('Relative error:', rel_err)
# print('Autogen time:', t1 - t0)
print('Solve time:', t1 - t0)
print('')
