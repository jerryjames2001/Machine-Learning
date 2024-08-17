import numpy as np
a=np.array([ [5,27,32],[14,53,62],[67,88,19] ])
u,s,vt=np.linalg.svd(a)
a_hat=u @ np.diag(s) @ vt
print(f"Orginal matrix\n{a}")
print(f"Singular value\n{s}")
print(f"Reconstructed matrix\n{a_hat}")