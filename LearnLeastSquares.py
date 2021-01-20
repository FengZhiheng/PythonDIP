

import numpy as np
import pandas as pd

X = np.random.randint(100,2)

X_DF = pd.DataFrame(data=X)

xbat =X_DF[:,2].mean