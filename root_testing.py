from poly import *

poly1 = poly([(100 + 30j), 1]) * poly([(100 - 30j), 1]) * poly([(2091 + 4039j), 1]) * poly([(2091 - 4039j), 1]) * poly([0, 1]) * poly([0, 1]) * poly([-400, 1]) 

# Complete
poly2 = poly([(0.0061652364526995915+0j), (-0.15703803937517294+0j), 1])
poly2_roots = [(0.07851901968758647+0j), (0.07851901968758647+0j)]

poly3 = poly([(-2.0329929352016895e+46+0j), (4.6074776066966756e+45+0j), (-2.8149275313239648e+44+0j), (1.7232900636595777e+41+0j), (1.753470178488559e+38+0j), (1.5162837879777032e+35+0j), (3.690172287974137e+32+0j), (-1.5610651329014487e+29+0j), (-2.5453582435211037e+26+0j), (-1.914824175192864e+23+0j), (-1.999356052571492e+20+0j), (-4.189609058991948e+16+0j), (13250777879930.385+0j), (3497366848.737716+0j), (3792.3283982909375+0j), 1])
poly3_roots = [(737.5504550420529+0j), (-1258.043481242107-0.1795066596232439j), (-1258.043481242107+0.1795066596232439j), (0.008727877200109596-1052.5593274967691j), (0.008727877200109596+1052.5593274967691j), (3977.3286200634852+0j), (8.245570792597876+2.2311916758674357j), (8.245570792597876-2.2311916758674357j), (838.3018391845926+0j), (0.35867508670257586-1250.9229528604917j), (0.35867508670257586+1250.9229528604917j), (-0.09183723360664127+59239.25413075491j), (-0.09183723360664127-59239.25413075491j), (-3423.232311571321+219.64706440370387j), (-3423.232311571321-219.64706440370387j)]

poly4 = poly([(-2.7018805671010557e+22+0j), (-1.5716623169295784e+23+0j), (-2.4443847899782123e+23+0j), (-4.449801966120565e+22+0j), (-5.664565973909162e+21+0j), (-3.773598542509574e+20+0j), (-6.581088086897592e+18+0j), (1.344647267861924e+17+0j), (-68493284034870.11+0j), (-2470364011305.509+0j), (-3886987920.265117+0j), (696769.2139345679+0j), 1])
poly4_roots = [(6107.370459723448+0j), (-0.35358691538379516-0.025101217985403275j), (-0.35358691538379516+0.025101217985403275j), (125.7892328786789-0.1347258370258997j), (125.7892328786789+0.1347258370258997j), (-2.6956978031119014-7.982302346478302j), (-2.6956978031119014+7.982302346478302j), (-702298.8690305309+0j), (-16.064158001634393+0j), (-16.064158001634393+0j), (-395.53347203871823-128.5120863713442j), (-395.53347203871823+128.5120863713442j)]

poly5 = poly([(-6.216709596597289e+32+0j), (-4.73601644828052e+34+0j), (9.248450422097024e+34+0j), (3.265264879003842e+34+0j), (-1.4754293144675006e+35+0j), (5.364096722541562e+34+0j), (-5.980346788672411e+32+0j), (-6.430995273069033e+29+0j), (1.3164751994105423e+28+0j), (2.69620524155744e+25+0j), (9.848461252151501e+21+0j), (1.732055679825955e+19+0j), (1876985607423356.8+0j), (48180630591.95877+0j), (-473832.6038101468+0j), 1])
poly5_roots = [(-0.012807657226288757+0j), (-374.3629853005646+0.7293989040027405j), (-374.3629853005646-0.7293989040027405j), (-0.8055095251182488+0j), (-15564.246893599515-3948.5243549764577j), (-15564.246893599515+3948.5243549764577j), (118.01385215604904-0.28278720553374226j), (118.01385215604904+0.28278720553374226j), (2.2876850792727277+0j), (0.6818186293643212+0.2055112842062053j), (0.6818186293643212-0.2055112842062053j), (252691.1970255266-0.004281560955700871j), (252691.1970255266+0.004281560955700871j), (44.28440371296966+1270.592364994047j), (44.28440371296966-1270.592364994047j)]

poly6 = poly([(-3.5494621908413655e+18+0j), (-4.4906709691588884e+18+0j), (-1.4580916143619953e+18+0j), (1208709117317800.5+0j), (1035807857022.1539+0j), (-533329274.85851234+0j), (-281960.6496382324+0j), 1])
poly6_roots = [(283826.8049441697+0j), (1110.9985160251522-0.1516505786768182j), (1110.9985160251522+0.1516505786768182j), (-2042.5391603827593-25.328645653569275j), (-2042.5391603827593+25.328645653569275j), (-1.5370086110311385-0.2564167215636021j), (-1.5370086110311385+0.2564167215636021j)]

poly7 = poly([(5.95874264132697e+16+0j), (-2.6402462259038e+18+0j), (1.614790434169545e+20+0j), (3826951491226745+0j), (29795828775.067806+0j), (168780.9107124116+0j), 1])
poly7_roots = [(-84390.45569850973+0.0016981140601646798j), (-84390.45569850973-0.0016981140601646798j), (0.008175198958141273+0.017383217631228236j), (0.008175198958141273-0.017383217631228236j), (-0.007832895038540236-150579.1482165251j), (-0.007832895038540236+150579.1482165251j)]

test_on = poly7

# a = [1, 2, 3, 4, 5]
# b = [0] * (4+1)
# print(a[1:len(a)])
# print(len(b))
# a = 1e15
# b = a + 1
# print(a - b)


# div = poly([-(0.008175198958141274-0.017383217631228236j), 1])
div = poly([-(-84390.45569850973-0.0016981140601646798j), 1])

(out, rem) = poly7.synthetic_division(div)
print('output pol', out.coeff_list)
print('remainder', rem)
print('eval at root:', poly7.evaluate((0.008175198958141274-0.017383217631228236j)))


result = poly7.comp_horner(-84390.45569850973+0.0016981140601646798j)
result2 = poly7.evaluate(-84390.45569850973+0.0016981140601646798j)
print('evaluate result', result2)
print('comp horner result:', result)

# print('Testing Root Finder')
# print('poly:', test_on.coeff_list)
# roots = test_on.find_roots(verbose=True, rel_tol=1E-10)
# print('')
# print('Final Result')
# print('Roots found:', roots)


