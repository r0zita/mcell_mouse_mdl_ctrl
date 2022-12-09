 #!/usr/bin/python

import sys
import numpy as np

#dont change these
ac1c2=7.0
bc2c1=1.0
ac2c3=6.0
bc3c2=2.0
ac3o1=5.0
bo1c3=3.0

k3_multiplier = 2.0

alpha_template = np.loadtxt('alpha_template.txt')
a_col0=alpha_template[:,0]
a_col1=alpha_template[:,1]

beta_template = np.loadtxt('beta_template.txt')
b_col0=beta_template[:,0]
b_col1=beta_template[:,1]

k3_template = np.loadtxt('k3_template.txt')
k3_col0=k3_template[:,0]
k3_col1=k3_template[:,1]

np.savetxt("ac1c2_template.txt", np.c_[a_col0,a_col1*ac1c2], fmt='%.8f %.6f')
np.savetxt("bc2c1_template.txt", np.c_[b_col0,b_col1*bc2c1], fmt='%.8f %.6f')
np.savetxt("ac2c3_template.txt", np.c_[a_col0,a_col1*ac2c3], fmt='%.8f %.6f')
np.savetxt("bc3c2_template.txt", np.c_[b_col0,b_col1*bc3c2], fmt='%.8f %.6f')
np.savetxt("ac3o1_template.txt", np.c_[a_col0,a_col1*ac3o1], fmt='%.8f %.6f')
np.savetxt("bo1c3_template.txt", np.c_[b_col0,b_col1*bo1c3], fmt='%.8f %.6f')

np.savetxt("k3_control_short_template.txt", np.c_[k3_col0,k3_col1*k3_multiplier], fmt='%.8f %.2f')


