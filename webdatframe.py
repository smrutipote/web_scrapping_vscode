import vspractice
import pandas as pd

data={'PhoneNumber':vspractice.phone,
      'Pincode':vspractice.pincode}

df=pd.DataFrame(data)
print(df)