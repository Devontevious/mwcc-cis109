with open ("application.log", "r") as file:
    content = file.read()
    
for line in content.split('\n'):
    timestamp = line[:19]
    toks = line.split('|')
    status = toks[1].strip().upper()
    if status.find("WARNING") != -1 or status.find("ERROR") != -1:
        log_message = " | ".join([timestamp, status, toks[2].strip()])
        print(log_message)