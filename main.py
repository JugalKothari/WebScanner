from general import *
from domain_name import *
from ip_address import *
from nmap import get_nmap
from robots_txt import *
from whois import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def gather_info(name, url):
    fullurl="https://"+url
    domain_name = get_domain_name(fullurl)
    get_ip_address(url)
    ip_address=str(input('Enter ip address'))
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(url)
    create_report(name, fullurl, domain_name, nmap, robots_txt,whois)

def create_report(name, full_url, domain_name, nmap, robots_txt,whois):
    project_dir= ROOT_DIR +'/'+name
    create_dir(project_dir)
    write_file(project_dir + 'full_url.txt', full_url)
    write_file (project_dir + 'domain_name.txt', domain_name)
    write_file(project_dir + 'nmap.txt', nmap)
    write_file(project_dir + 'robots_txt.txt', robots_txt)
    write_file(project_dir + 'whois.txt', whois)
    
gather_info('youtube', 'www.youtube.com')