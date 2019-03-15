# Meant to run interactively (python -i) use hset variable to test functionality
from NeuroPy import NeuroPy
import time

hset = NeuroPy('COM4')
hset.start()
time.sleep(8)
print('Ready...')
