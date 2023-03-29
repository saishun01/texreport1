import numpy as np

mu = 1.25663706 * 10**(-6)
e = 1.60217662 * 10**(-19)
hbar = 1.054571817 * 10**(-34)
me = 9.10938356 * 10**(-31)
a0 = 0.529117210903 * 10**(-10)

#分裂エネルギー
D_joule = mu*e**2*hbar**2/(16*16*np.pi*me**2*a0**3)
D_meV = D_joule*6.242*10**(18)*10**3
print(D_meV)

#実際のエネルギー誤差
h = 6.62607015 * 10**(-34)
c = 2.99792458 * 10**8
lam = 700 * 10**(-9)
dlam = 0.1 * 10**(-9)
E_joule = h*c*dlam/lam**2
E_meV = E_joule*6.242*10**(18)*10**3
print(E_meV)