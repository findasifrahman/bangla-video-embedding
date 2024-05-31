from functions import *
import time
import datetime

print(datetime, datetime.datetime.now())

t0 = time.time()
getVidId()
ti = time.time()
print("step 1: done")
print("---> Video IDS downloaded in: ", ti-t0, " seconds")

t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print("step 2: done")
print("---> Video Transcripts downloaded in: ", t1-t0, " seconds")

to = time.time()
transformData()
t1 = time.time()
print("step 3: done")
print("---> Data transformed in: ", t1-to, " seconds")

t0 = time.time()
createTextEmbeddings()
t1 = time.time()
print("step 4: done")
print("---> Text embeddings created in: ", t1-t0, " seconds")