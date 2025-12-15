import pandas as pd
from autoclean import AutoClean

df = pd.DataFrame({
    " First Name ": ["John", "Sara", "Sara"],
    "AGE ": [25, None, None],
    "notes": [None, None, None],
    "salary": [5000, 6000, 7000]
})

print("\n===== Running AutoClean =====")
cleaner = AutoClean(df, verbose=True)
cleaned_df = cleaner.run()

print("\nCleaned DataFrame:")
print(cleaned_df)
