investment_percentage = int(0.15)
stock_roi = int(.07)
bond_roi = int(.05)

import numpy_financial as np
# Calculate FV of current plan
FV_Current = np.fv(.05/12,10*12,-100,-100)

print(FV_Current)
# Calculate PMT to hit retirement goal
