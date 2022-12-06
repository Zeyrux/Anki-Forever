import psutil

for proc in psutil.process_iter():
    proc_info = proc.as_dict(["exe", "name"])
    print(proc_info)
