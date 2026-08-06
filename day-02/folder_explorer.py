import os
# Where am I right now?
print("Current folder:", os.getcwd())

# What is in here?
print("\nContents:")
for item in os.listdir():
    print(" -", item)