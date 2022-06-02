from sqlite3 import Timestamp
import uuid
import time
import random
from uuid import uuid1, getnode

# make a UUID based on the host ID and current time
x = uuid.uuid1()
print(x)
# make a UUID using an MD5 hash of a namespace UUID and a name
Y = uuid.NAMESPACE_DNS
print(Y)
# make a random UUID
z = uuid.uuid4()
print(z)
f = uuid.uuid1(node=None, clock_seq=None)
print(f)


