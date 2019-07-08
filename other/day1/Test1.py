# # -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

dates = pd.date_range("20190909" ,periods=6)
df = pd.DataFrame(np.random.rand(6,4) ,index=dates ,columns=list("ABCD"))
print(df)