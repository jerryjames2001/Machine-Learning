import numpy as np
even=np.arange(2,31,2)
print(f"Elements from index 2->8 :{even[2:8:2]}")
print(f"Last 3 elements :{even[-3:]}")
print(f"Alternate elements :{even[::2]}")
print(f"Last 3 alternative elements :{even[-6::2]}")