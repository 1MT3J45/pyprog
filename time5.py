#!/usr/bin/python
import time

# measure process time
t0 = time.clock()
time.sleep(2.5)

print time.clock() - t0, "seconds process time"

# measure wall time
t0 = time.time()

time.sleep(2.5)
print time.time() - t0, "seconds wall time"
