import os.path
import time
from math import *
from math import sqrt
from numpy.linalg import *
import numpy as np
import matplotlib.pyplot as plt
import cmath
from matplotlib.collections import LineCollection
import matplotlib.cm as cm
from draw_phononTB_HAN import *
#from numeric import *




lat = [[2.04181100000000, -3.53652039145302,   0.00000000000000], [ 2.04181100000000,  3.53652039145302,   0.00000000000000], [0.00000000000000,  0.00000000000000,  17.55041300000000]]
orb = [[2.0/3 ,   1.0/3 , 0.83038900000000], [2.0/3 ,   1.0/3 , 0.66961100000000], [1.0/3 ,   2.0/3 , 0.59679800000000],[1.0/3 ,   2.0/3 , 0.90320200000000]]
mass = [24.0, 24.0, 12.0, 12.0]
fc_nn  =  [[-1.0,0.0],[0.0,-1.0]]
fc_nn1 = [[-22.19684176,   -7.699687431],[-7.699687431,   -13.306]]
fc_nn2 = [[-22.19684176 ,    7.699687431],[ 7.699687431,   -13.306]]
fc_nn3 = [[-8.860588573805234,    -0.000000000000000],[-0.000000000000000 ,  -26.642257254446765]]
fc_nnn = [[0.1,0.0],[0.0,0.3]]
V_info = [-1.0, -0.2]

###############################################################################
FC = ForceConstant(3, 4)

FC.set_geometry(lat, orb, mass)
FC.set_hopping(0,1,[0.0,0.0,0.0],V_info)

FC.set_hopping(0,2,[0.0,0.0,0.0],V_info)
FC.set_hopping(0,2,[1.0,0.0,0.0],V_info)
FC.set_hopping(0,2,[0.0,-1.0,0.0],V_info)

FC.set_hopping(1,3,[0.0,0.0,0.0],V_info)
FC.set_hopping(1,3,[1.0,0.0,0.0],V_info)
FC.set_hopping(1,3,[0.0,-1.0,0.0],V_info)

#FC_dice.set_hopping(0,0,[0.0,0.0],V_info_hex2)
#FC_dice.set_hopping(1,1,[0.0,0.0],V_info_hex2)

#FC_dice.set_hopping(1,1,[-1.0,-1.0],V_info2_hex)
#FC_dice.set_hopping(1,1,[0.0,1.0],V_info2_hex)
#FC_dice.set_hopping(1,1,[1.0,0.0],V_info2_hex)
#FC_dice.set_hopping(0,0,[-1.0,0.0],V_info2_           hex)
#FC_dice.set_hopping(0,0,[1.0,1.0],V_info2_hex)
#FC_dice.set_hopping(0,0,[0.0,-1.0],V_info2_hex)

FC.set_acoustic_sum_rule()
#FC_dice.set_acoustic_sum_rule()

FC.print_info()


###############################################################################
alpha0 = [[0.0,0.0,0.02]]
alpha4 = [[0.0,0.0,0.00],[0.0,0.0,0.00],[0.0,0.0,0.02], [0.0,0.0,-0.02]]
q_path = [[0, 0, 0.0], [0.5, 0.0, 0.0], [1.0/3, 1.0/3, 0.0], [0.0, 0, 0.0]]

q_spacing = 100


q_grid = ['slice',[51, 51, 1], 0.0]  #### [q_slice mode, [nx, ny, nz], fixed_qpoints]
q_path_K = [[1.0/3+0.01,1.0/3-0.01],[1.0/3+0.01,1.0/3+0.01],[1.0/3-0.01,1.0/3+0.01],[1.0/3-0.01,1.0/3-0.01],[1.0/3+0.01,1.0/3-0.01]]
q_path_Kp = [[2.0/3+0.01,-1.0/3-0.01],[2.0/3+0.01,-1.0/3+0.01],[2.0/3-0.01,-1.0/3+0.01],[2.0/3-0.01,-1.0/3-0.01],[2.0/3+0.01,-1.0/3-0.01]]
q_path_X = [[1.0/2+0.0001,0.0/2-0.0001],[1.0/2+0.0001,0.0/2+0.0001],[1.0/2-0.0001,0.0/2+0.0001],[1.0/2-0.0001,0.0/2-0.0001],[1.0/2+0.0001,0.0/2-0.0001]]
q_grid_berry_K = ['berryphase', q_path_K, 50]
q_grid_berry_X = ['berryphase', q_path_X, 50]
print FC.recip_vec
#q_grid = ['berrycurv', [-2.5471742, 2.5471742], [-1.47061171, 1.47061171], [2, 0.0], 201, 201]

###############################################################################
DM = DynamicalMatrix('IS_test', FC, alpha0)


DM.get_phonon_band(q_path,q_spacing)
DM.draw_phonon_band()
#DM.make_phband_PROCAR_format(q_grid)
#DM.get_3Dplot_data(14)


###############################################################################
band_range = [int(i) for i in range(12,20)] ; print '# of bands = ' + str(len(band_range)) + ' Detail bands = ' + str(band_range)
#CTI = ComputeTopologicalInvariants('IS_test',band_range, q_grid)
#CTI.get_Willsons_loop()
#CTI_hex.calculate_Berry_phase()
