import json, sys
from src.remediation import Signal, recommend
for line in sys.stdin:
    if line.strip():
        payload=json.loads(line); approved,reasons=recommend(Signal(**payload))
        print(json.dumps({"input":payload,"approved":approved,"reasons":reasons}))
