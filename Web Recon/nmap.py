import os


def get_nmap(options,ip_address):
    command = "nmap " + options + " " + ip_address
    process = os.popen(command)
    results = str(process.read())
    return results