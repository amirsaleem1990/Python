import pandas as pd
processors_qty = !grep -c ^processor /proc/cpuinfo
processors_qty = int(processors_qty[0])
df = pd.DataFrame(columns = list(map(lambda x: "CPU_" + str(x), range(1, processors_qty+1))))
import time
while True:
    try:
        time.sleep(1)
        cpu_status = !mpstat -P ALL 1 1 | awk '/Average:/ && $2 ~ /[0-9]/ {print $3}'
        print(cpu_status)
        df.loc[len(df)+1] = cpu_status
    except KeyboardInterrupt:
        break