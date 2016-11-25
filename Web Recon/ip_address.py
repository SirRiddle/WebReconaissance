import socket


def get_ip_address(domain_name):
    ip_address = socket.gethostbyname(domain_name)
    return ip_address