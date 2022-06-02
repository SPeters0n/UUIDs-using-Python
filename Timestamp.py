from datetime import datetime
import uuid
ID = uuid.uuid1()
now = datetime.now()

current_time = now.strftime('%H:%M:%S')
print(ID,now)


