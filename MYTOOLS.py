from mpmath import mp

mp.dps = 100
pi_valor = str(mp.pi)
PI_INT = pi_valor[2:] 

mp.dps = 100
e = mp.e
e_str = str(e)
integer_part, decimal_part = e_str.split('.')
E_INT = decimal_part

def pi_real(n):
    if 0<n<100:
        pi = '3.' + PI_INT[:n]
        return float(pi)

def e_real(n):
    if 0<n<100:
        e = '2.' + E_INT[:n]
        return float(e)

