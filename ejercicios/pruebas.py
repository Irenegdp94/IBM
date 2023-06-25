import numpy as np
import time



x = list(np.random.randint(low=1,high=500000,
size=99999999))

inicio = time.time()
# ------------- Código a medir -------------
# def constante(x:list) -> list: return x
# constante(x)



# ------------------------------------------

fin = time.time()
print(fin-inicio) 



