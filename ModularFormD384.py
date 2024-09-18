import numpy as np

def Y18k2(t):
    return [-8*np.exp(((3*1j)/4)*np.pi*t) - 24*np.exp(((11*1j)/4)*np.pi*t) - 40*np.exp(((19*1j)/4)*np.pi*t) - 80*np.exp(((27*1j)/4)*np.pi*t) - 96*np.exp(((35*1j)/4)*np.pi*t) - 88*np.exp(((43*1j)/4)*np.pi*t) - 144*np.exp(((51*1j)/4)*np.pi*t) - 120*np.exp(((59*1j)/4)*np.pi*t) - 136*np.exp(((67*1j)/4)*np.pi*t) - 248*np.exp(((75*1j)/4)*np.pi*t) - 168*np.exp(((83*1j)/4)*np.pi*t) - 224*np.exp(((91*1j)/4)*np.pi*t) - 312*np.exp(((99*1j)/4)*np.pi*t) - 216*np.exp(((107*1j)/4)*np.pi*t) - 288*np.exp(((115*1j)/4)*np.pi*t) - 336*np.exp(((123*1j)/4)*np.pi*t) - 264*np.exp(((131*1j)/4)*np.pi*t) - 280*np.exp(((139*1j)/4)*np.pi*t) - 456*np.exp(((147*1j)/4)*np.pi*t) - 384*np.exp(((155*1j)/4)*np.pi*t), 2*np.exp((1j/4)*np.pi*t) + 26*np.exp(((9*1j)/4)*np.pi*t) + 36*np.exp(((17*1j)/4)*np.pi*t) + 62*np.exp(((25*1j)/4)*np.pi*t) + 96*np.exp(((33*1j)/4)*np.pi*t) + 84*np.exp(((41*1j)/4)*np.pi*t) + 114*np.exp(((49*1j)/4)*np.pi*t) + 160*np.exp(((57*1j)/4)*np.pi*t) + 168*np.exp(((65*1j)/4)*np.pi*t) + 148*np.exp(((73*1j)/4)*np.pi*t) + 242*np.exp(((81*1j)/4)*np.pi*t) + 180*np.exp(((89*1j)/4)*np.pi*t) + 196*np.exp(((97*1j)/4)*np.pi*t) + 384*np.exp(((105*1j)/4)*np.pi*t) + 228*np.exp(((113*1j)/4)*np.pi*t) + 266*np.exp(((121*1j)/4)*np.pi*t) + 352*np.exp(((129*1j)/4)*np.pi*t) + 276*np.exp(((137*1j)/4)*np.pi*t) + 360*np.exp(((145*1j)/4)*np.pi*t) + 468*np.exp(((153*1j)/4)*np.pi*t), -4*np.exp(1j*np.pi*t) + 16*np.exp((3*1j)*np.pi*t) - 24*np.exp((5*1j)*np.pi*t) + 32*np.exp((7*1j)*np.pi*t) - 52*np.exp((9*1j)*np.pi*t) + 48*np.exp((11*1j)*np.pi*t) - 56*np.exp((13*1j)*np.pi*t) + 96*np.exp((15*1j)*np.pi*t) - 72*np.exp((17*1j)*np.pi*t) + 80*np.exp((19*1j)*np.pi*t) - 128*np.exp((21*1j)*np.pi*t) + 96*np.exp((23*1j)*np.pi*t) - 124*np.exp((25*1j)*np.pi*t) + 160*np.exp((27*1j)*np.pi*t) - 120*np.exp((29*1j)*np.pi*t) + 128*np.exp((31*1j)*np.pi*t) - 192*np.exp((33*1j)*np.pi*t) + 192*np.exp((35*1j)*np.pi*t) - 152*np.exp((37*1j)*np.pi*t) + 224*np.exp((39*1j)*np.pi*t), 1 - 8*np.exp((4*1j)*np.pi*t) + 24*np.exp((8*1j)*np.pi*t) - 32*np.exp((12*1j)*np.pi*t) + 24*np.exp((16*1j)*np.pi*t) - 48*np.exp((20*1j)*np.pi*t) + 96*np.exp((24*1j)*np.pi*t) - 64*np.exp((28*1j)*np.pi*t) + 24*np.exp((32*1j)*np.pi*t) - 104*np.exp((36*1j)*np.pi*t) + 144*np.exp((40*1j)*np.pi*t), -12*np.exp(((5*1j)/4)*np.pi*t) - 28*np.exp(((13*1j)/4)*np.pi*t) - 64*np.exp(((21*1j)/4)*np.pi*t) - 60*np.exp(((29*1j)/4)*np.pi*t) - 76*np.exp(((37*1j)/4)*np.pi*t) - 156*np.exp(((45*1j)/4)*np.pi*t) - 108*np.exp(((53*1j)/4)*np.pi*t) - 124*np.exp(((61*1j)/4)*np.pi*t) - 192*np.exp(((69*1j)/4)*np.pi*t) - 192*np.exp(((77*1j)/4)*np.pi*t) - 216*np.exp(((85*1j)/4)*np.pi*t) - 256*np.exp(((93*1j)/4)*np.pi*t) - 204*np.exp(((101*1j)/4)*np.pi*t) - 220*np.exp(((109*1j)/4)*np.pi*t) - 364*np.exp(((117*1j)/4)*np.pi*t) - 312*np.exp(((125*1j)/4)*np.pi*t) - 320*np.exp(((133*1j)/4)*np.pi*t) - 384*np.exp(((141*1j)/4)*np.pi*t) - 300*np.exp(((149*1j)/4)*np.pi*t) - 316*np.exp(((157*1j)/4)*np.pi*t), -16*np.exp(((7*1j)/4)*np.pi*t) - 48*np.exp(((15*1j)/4)*np.pi*t) - 48*np.exp(((23*1j)/4)*np.pi*t) - 64*np.exp(((31*1j)/4)*np.pi*t) - 112*np.exp(((39*1j)/4)*np.pi*t) - 96*np.exp(((47*1j)/4)*np.pi*t) - 144*np.exp(((55*1j)/4)*np.pi*t) - 208*np.exp(((63*1j)/4)*np.pi*t) - 144*np.exp(((71*1j)/4)*np.pi*t) - 160*np.exp(((79*1j)/4)*np.pi*t) - 240*np.exp(((87*1j)/4)*np.pi*t) - 240*np.exp(((95*1j)/4)*np.pi*t) - 208*np.exp(((103*1j)/4)*np.pi*t) - 304*np.exp(((111*1j)/4)*np.pi*t) - 288*np.exp(((119*1j)/4)*np.pi*t) - 256*np.exp(((127*1j)/4)*np.pi*t) - 480*np.exp(((135*1j)/4)*np.pi*t) - 336*np.exp(((143*1j)/4)*np.pi*t) - 304*np.exp(((151*1j)/4)*np.pi*t) - 432*np.exp(((159*1j)/4)*np.pi*t)]

def Y20k2(t):
    return [-(np.sqrt(2)*np.exp((1j/4)*np.pi*t)) - 3*np.sqrt(2)*np.exp(((9*1j)/4)*np.pi*t) + 2*np.sqrt(2)*np.exp(((17*1j)/4)*np.pi*t) + 11*np.sqrt(2)*np.exp(((25*1j)/4)*np.pi*t) - 10*np.sqrt(2)*np.exp(((41*1j)/4)*np.pi*t) + 7*np.sqrt(2)*np.exp(((49*1j)/4)*np.pi*t) - 16*np.sqrt(2)*np.exp(((65*1j)/4)*np.pi*t) - 6*np.sqrt(2)*np.exp(((73*1j)/4)*np.pi*t) - 9*np.sqrt(2)*np.exp(((81*1j)/4)*np.pi*t) + 10*np.sqrt(2)*np.exp(((89*1j)/4)*np.pi*t) + 18*np.sqrt(2)*np.exp(((97*1j)/4)*np.pi*t) + 14*np.sqrt(2)*np.exp(((113*1j)/4)*np.pi*t) - 11*np.sqrt(2)*np.exp(((121*1j)/4)*np.pi*t) + 22*np.sqrt(2)*np.exp(((137*1j)/4)*np.pi*t) - 16*np.sqrt(2)*np.exp(((145*1j)/4)*np.pi*t) + 6*np.sqrt(2)*np.exp(((153*1j)/4)*np.pi*t) + 3*np.sqrt(2)*np.exp(((169*1j)/4)*np.pi*t), 3*np.exp(((9*1j)/8)*np.pi*t) - 11*np.exp(((25*1j)/8)*np.pi*t) + 10*np.exp(((41*1j)/8)*np.pi*t) + 6*np.exp(((73*1j)/8)*np.pi*t) - 10*np.exp(((89*1j)/8)*np.pi*t) + 11*np.exp(((121*1j)/8)*np.pi*t) - 22*np.exp(((137*1j)/8)*np.pi*t) - 6*np.exp(((153*1j)/8)*np.pi*t) - 3*np.exp(((169*1j)/8)*np.pi*t) + 48*np.exp(((185*1j)/8)*np.pi*t) - 26*np.exp(((233*1j)/8)*np.pi*t) - 16*np.exp(((265*1j)/8)*np.pi*t) - 10*np.exp(((281*1j)/8)*np.pi*t) + 26*np.exp(((313*1j)/8)*np.pi*t) + 19*np.exp(((361*1j)/8)*np.pi*t), np.exp((1j/8)*np.pi*t) - 2*np.exp(((17*1j)/8)*np.pi*t) - 7*np.exp(((49*1j)/8)*np.pi*t) + 16*np.exp(((65*1j)/8)*np.pi*t) + 9*np.exp(((81*1j)/8)*np.pi*t) - 18*np.exp(((97*1j)/8)*np.pi*t) - 14*np.exp(((113*1j)/8)*np.pi*t) + 16*np.exp(((145*1j)/8)*np.pi*t) + 14*np.exp(((193*1j)/8)*np.pi*t) - 33*np.exp(((225*1j)/8)*np.pi*t) + 30*np.exp(((241*1j)/8)*np.pi*t) + 2*np.exp(((257*1j)/8)*np.pi*t) - 13*np.exp(((289*1j)/8)*np.pi*t) - 48*np.exp(((305*1j)/8)*np.pi*t) + 18*np.exp(((337*1j)/8)*np.pi*t) + 34*np.exp(((353*1j)/8)*np.pi*t), -4*np.sqrt(2)*np.exp(((5*1j)/4)*np.pi*t) + 4*np.sqrt(2)*np.exp(((13*1j)/4)*np.pi*t) + 4*np.sqrt(2)*np.exp(((29*1j)/4)*np.pi*t) + 12*np.sqrt(2)*np.exp(((37*1j)/4)*np.pi*t) - 12*np.sqrt(2)*np.exp(((45*1j)/4)*np.pi*t) - 4*np.sqrt(2)*np.exp(((53*1j)/4)*np.pi*t) - 12*np.sqrt(2)*np.exp(((61*1j)/4)*np.pi*t) + 8*np.sqrt(2)*np.exp(((85*1j)/4)*np.pi*t) - 20*np.sqrt(2)*np.exp(((101*1j)/4)*np.pi*t) + 20*np.sqrt(2)*np.exp(((109*1j)/4)*np.pi*t) + 12*np.sqrt(2)*np.exp(((117*1j)/4)*np.pi*t) + 24*np.sqrt(2)*np.exp(((125*1j)/4)*np.pi*t) - 20*np.sqrt(2)*np.exp(((149*1j)/4)*np.pi*t) - 12*np.sqrt(2)*np.exp(((157*1j)/4)*np.pi*t) + 4*np.sqrt(2)*np.exp(((173*1j)/4)*np.pi*t) - 20*np.sqrt(2)*np.exp(((181*1j)/4)*np.pi*t), 4*np.exp(((5*1j)/8)*np.pi*t) - 12*np.exp(((37*1j)/8)*np.pi*t) + 4*np.exp(((53*1j)/8)*np.pi*t) - 8*np.exp(((85*1j)/8)*np.pi*t) + 20*np.exp(((101*1j)/8)*np.pi*t) - 12*np.exp(((117*1j)/8)*np.pi*t) + 20*np.exp(((149*1j)/8)*np.pi*t) + 20*np.exp(((181*1j)/8)*np.pi*t) - 28*np.exp(((197*1j)/8)*np.pi*t) + 4*np.exp(((229*1j)/8)*np.pi*t) - 28*np.exp(((245*1j)/8)*np.pi*t) - 12*np.exp(((261*1j)/8)*np.pi*t) - 28*np.exp(((277*1j)/8)*np.pi*t) + 4*np.exp(((293*1j)/8)*np.pi*t) + 44*np.exp(((325*1j)/8)*np.pi*t), -4*np.exp(((13*1j)/8)*np.pi*t) - 4*np.exp(((29*1j)/8)*np.pi*t) + 12*np.exp(((45*1j)/8)*np.pi*t) + 12*np.exp(((61*1j)/8)*np.pi*t) - 20*np.exp(((109*1j)/8)*np.pi*t) - 24*np.exp(((125*1j)/8)*np.pi*t) + 12*np.exp(((157*1j)/8)*np.pi*t) - 4*np.exp(((173*1j)/8)*np.pi*t) + 40*np.exp(((205*1j)/8)*np.pi*t) + 8*np.exp(((221*1j)/8)*np.pi*t) - 20*np.exp(((269*1j)/8)*np.pi*t) + 28*np.exp(((317*1j)/8)*np.pi*t) - 36*np.exp(((333*1j)/8)*np.pi*t) - 36*np.exp(((349*1j)/8)*np.pi*t) + 24*np.exp(((365*1j)/8)*np.pi*t)]

def Y23k2(t):
    return [-8*np.sqrt(2)*np.exp(((7*1j)/8)*np.pi*t) - 24*np.sqrt(2)*np.exp(((23*1j)/8)*np.pi*t) - 24*np.sqrt(2)*np.exp(((39*1j)/8)*np.pi*t) - 40*np.sqrt(2)*np.exp(((55*1j)/8)*np.pi*t) - 72*np.sqrt(2)*np.exp(((71*1j)/8)*np.pi*t) - 56*np.sqrt(2)*np.exp(((87*1j)/8)*np.pi*t) - 104*np.sqrt(2)*np.exp(((103*1j)/8)*np.pi*t) - 144*np.sqrt(2)*np.exp(((119*1j)/8)*np.pi*t) - 80*np.sqrt(2)*np.exp(((135*1j)/8)*np.pi*t) - 152*np.sqrt(2)*np.exp(((151*1j)/8)*np.pi*t) - 168*np.sqrt(2)*np.exp(((167*1j)/8)*np.pi*t) - 120*np.sqrt(2)*np.exp(((183*1j)/8)*np.pi*t) - 200*np.sqrt(2)*np.exp(((199*1j)/8)*np.pi*t) - 168*np.sqrt(2)*np.exp(((215*1j)/8)*np.pi*t) - 160*np.sqrt(2)*np.exp(((231*1j)/8)*np.pi*t) - 216*np.sqrt(2)*np.exp(((247*1j)/8)*np.pi*t) - 264*np.sqrt(2)*np.exp(((263*1j)/8)*np.pi*t) - 224*np.sqrt(2)*np.exp(((279*1j)/8)*np.pi*t) - 232*np.sqrt(2)*np.exp(((295*1j)/8)*np.pi*t) - 312*np.sqrt(2)*np.exp(((311*1j)/8)*np.pi*t) - 216*np.sqrt(2)*np.exp(((327*1j)/8)*np.pi*t) - 400*np.sqrt(2)*np.exp(((343*1j)/8)*np.pi*t) - 360*np.sqrt(2)*np.exp(((359*1j)/8)*np.pi*t), 8*np.sqrt(2)*np.exp(((15*1j)/8)*np.pi*t) + 32*np.sqrt(2)*np.exp(((31*1j)/8)*np.pi*t) + 48*np.sqrt(2)*np.exp(((47*1j)/8)*np.pi*t) + 56*np.sqrt(2)*np.exp(((63*1j)/8)*np.pi*t) + 80*np.sqrt(2)*np.exp(((79*1j)/8)*np.pi*t) + 72*np.sqrt(2)*np.exp(((95*1j)/8)*np.pi*t) + 72*np.sqrt(2)*np.exp(((111*1j)/8)*np.pi*t) + 128*np.sqrt(2)*np.exp(((127*1j)/8)*np.pi*t) + 120*np.sqrt(2)*np.exp(((143*1j)/8)*np.pi*t) + 104*np.sqrt(2)*np.exp(((159*1j)/8)*np.pi*t) + 168*np.sqrt(2)*np.exp(((175*1j)/8)*np.pi*t) + 192*np.sqrt(2)*np.exp(((191*1j)/8)*np.pi*t) + 168*np.sqrt(2)*np.exp(((207*1j)/8)*np.pi*t) + 224*np.sqrt(2)*np.exp(((223*1j)/8)*np.pi*t) + 240*np.sqrt(2)*np.exp(((239*1j)/8)*np.pi*t) + 144*np.sqrt(2)*np.exp(((255*1j)/8)*np.pi*t) + 272*np.sqrt(2)*np.exp(((271*1j)/8)*np.pi*t) + 336*np.sqrt(2)*np.exp(((287*1j)/8)*np.pi*t) + 200*np.sqrt(2)*np.exp(((303*1j)/8)*np.pi*t) + 280*np.sqrt(2)*np.exp(((319*1j)/8)*np.pi*t) + 264*np.sqrt(2)*np.exp(((335*1j)/8)*np.pi*t) + 240*np.sqrt(2)*np.exp(((351*1j)/8)*np.pi*t) + 368*np.sqrt(2)*np.exp(((367*1j)/8)*np.pi*t), -6*np.exp(1j*np.pi*t) + 4*np.exp((3*1j)*np.pi*t) - 8*np.exp((5*1j)*np.pi*t) + 48*np.exp((7*1j)*np.pi*t) - 42*np.exp((9*1j)*np.pi*t) + 20*np.exp((11*1j)*np.pi*t) - 24*np.exp((13*1j)*np.pi*t) + 48*np.exp((15*1j)*np.pi*t) - 108*np.exp((17*1j)*np.pi*t) + 36*np.exp((19*1j)*np.pi*t) - 32*np.exp((21*1j)*np.pi*t) + 144*np.exp((23*1j)*np.pi*t) - 126*np.exp((25*1j)*np.pi*t) + 40*np.exp((27*1j)*np.pi*t) - 56*np.exp((29*1j)*np.pi*t) + 192*np.exp((31*1j)*np.pi*t) - 120*np.exp((33*1j)*np.pi*t) + 64*np.exp((35*1j)*np.pi*t) - 72*np.exp((37*1j)*np.pi*t) + 144*np.exp((39*1j)*np.pi*t) - 252*np.exp((41*1j)*np.pi*t) + 84*np.exp((43*1j)*np.pi*t) - 56*np.exp((45*1j)*np.pi*t), 1 + 10*np.exp((2*1j)*np.pi*t) - 18*np.exp((4*1j)*np.pi*t) + 12*np.exp((6*1j)*np.pi*t) - 34*np.exp((8*1j)*np.pi*t) + 24*np.exp((10*1j)*np.pi*t) - 28*np.exp((12*1j)*np.pi*t) + 80*np.exp((14*1j)*np.pi*t) - 66*np.exp((16*1j)*np.pi*t) + 70*np.exp((18*1j)*np.pi*t) - 56*np.exp((20*1j)*np.pi*t) + 60*np.exp((22*1j)*np.pi*t) - 60*np.exp((24*1j)*np.pi*t) + 72*np.exp((26*1j)*np.pi*t) - 144*np.exp((28*1j)*np.pi*t) + 80*np.exp((30*1j)*np.pi*t) - 130*np.exp((32*1j)*np.pi*t) + 180*np.exp((34*1j)*np.pi*t) - 126*np.exp((36*1j)*np.pi*t) + 108*np.exp((38*1j)*np.pi*t) - 120*np.exp((40*1j)*np.pi*t) + 96*np.exp((42*1j)*np.pi*t) - 140*np.exp((44*1j)*np.pi*t) + 240*np.exp((46*1j)*np.pi*t), -7*np.sqrt(2)*np.exp(((9*1j)/8)*np.pi*t) - 21*np.sqrt(2)*np.exp(((25*1j)/8)*np.pi*t) - 42*np.sqrt(2)*np.exp(((41*1j)/8)*np.pi*t) - 36*np.sqrt(2)*np.exp(((57*1j)/8)*np.pi*t) - 74*np.sqrt(2)*np.exp(((73*1j)/8)*np.pi*t) - 90*np.sqrt(2)*np.exp(((89*1j)/8)*np.pi*t) - 64*np.sqrt(2)*np.exp(((105*1j)/8)*np.pi*t) - 111*np.sqrt(2)*np.exp(((121*1j)/8)*np.pi*t) - 138*np.sqrt(2)*np.exp(((137*1j)/8)*np.pi*t) - 126*np.sqrt(2)*np.exp(((153*1j)/8)*np.pi*t) - 157*np.sqrt(2)*np.exp(((169*1j)/8)*np.pi*t) - 144*np.sqrt(2)*np.exp(((185*1j)/8)*np.pi*t) - 132*np.sqrt(2)*np.exp(((201*1j)/8)*np.pi*t) - 256*np.sqrt(2)*np.exp(((217*1j)/8)*np.pi*t) - 234*np.sqrt(2)*np.exp(((233*1j)/8)*np.pi*t) - 164*np.sqrt(2)*np.exp(((249*1j)/8)*np.pi*t) - 208*np.sqrt(2)*np.exp(((265*1j)/8)*np.pi*t) - 282*np.sqrt(2)*np.exp(((281*1j)/8)*np.pi*t) - 200*np.sqrt(2)*np.exp(((297*1j)/8)*np.pi*t) - 314*np.sqrt(2)*np.exp(((313*1j)/8)*np.pi*t) - 384*np.sqrt(2)*np.exp(((329*1j)/8)*np.pi*t) - 192*np.sqrt(2)*np.exp(((345*1j)/8)*np.pi*t) - 343*np.sqrt(2)*np.exp(((361*1j)/8)*np.pi*t), np.sqrt(2)*np.exp((1j/8)*np.pi*t) + 18*np.sqrt(2)*np.exp(((17*1j)/8)*np.pi*t) + 20*np.sqrt(2)*np.exp(((33*1j)/8)*np.pi*t) + 57*np.sqrt(2)*np.exp(((49*1j)/8)*np.pi*t) + 48*np.sqrt(2)*np.exp(((65*1j)/8)*np.pi*t) + 61*np.sqrt(2)*np.exp(((81*1j)/8)*np.pi*t) + 98*np.sqrt(2)*np.exp(((97*1j)/8)*np.pi*t) + 114*np.sqrt(2)*np.exp(((113*1j)/8)*np.pi*t) + 84*np.sqrt(2)*np.exp(((129*1j)/8)*np.pi*t) + 112*np.sqrt(2)*np.exp(((145*1j)/8)*np.pi*t) + 192*np.sqrt(2)*np.exp(((161*1j)/8)*np.pi*t) + 116*np.sqrt(2)*np.exp(((177*1j)/8)*np.pi*t) + 194*np.sqrt(2)*np.exp(((193*1j)/8)*np.pi*t) + 180*np.sqrt(2)*np.exp(((209*1j)/8)*np.pi*t) + 147*np.sqrt(2)*np.exp(((225*1j)/8)*np.pi*t) + 242*np.sqrt(2)*np.exp(((241*1j)/8)*np.pi*t) + 258*np.sqrt(2)*np.exp(((257*1j)/8)*np.pi*t) + 192*np.sqrt(2)*np.exp(((273*1j)/8)*np.pi*t) + 307*np.sqrt(2)*np.exp(((289*1j)/8)*np.pi*t) + 240*np.sqrt(2)*np.exp(((305*1j)/8)*np.pi*t) + 212*np.sqrt(2)*np.exp(((321*1j)/8)*np.pi*t) + 338*np.sqrt(2)*np.exp(((337*1j)/8)*np.pi*t) + 354*np.sqrt(2)*np.exp(((353*1j)/8)*np.pi*t)]

