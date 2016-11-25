from domain_name import *
from general import *
from get_robots import *
from ip_address import *
from nmap import *
from whois import *


ROOT_DIR = 'WebsiteLogs'
create_dir(ROOT_DIR)

def get_info(dir_name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap("-F",ip_address)
    robots_txt = get_rtxt(url)
    whois = get_whois(domain_name)
    log_report(dir_name,url,domain_name,nmap,robots_txt,whois)


def log_report(dir_name, url, domain_name, nmap, robots_txt, whois):
    dir = ROOT_DIR + '/' + dir_name
    create_dir(dir)
    write_file(dir+"/URL",url)
    write_file(dir+"/domain_name", domain_name)
    write_file(dir+"/nmap", nmap)
    write_file(dir+"/robots", robots_txt)
    write_file(dir+"/whois", whois)