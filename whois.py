import os
def get_whois(url):
    command="Whois\\whois -v "+url
    process = os.popen(command)
    results = str(process.read())
    return results

#print(get_whois('www.youtube.com'))
