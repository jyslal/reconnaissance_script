import subprocess
import os
import ipaddress

def portScanning(cmd):
    port_found = False
    with subprocess.Popen(cmd,stdout= subprocess.PIPE, text=True, bufsize=1) as nmap:
        for lin in nmap.stdout:
                if "/tcp" in lin.lower() and "open" in lin.lower():
                    print("-",lin,end="")
                    port_found = True
    
    if not port_found:
        print("0 open port, sorry")

def body():
    cible= input("veuillez saisir votre cible à tester: ")
    while True:
        try:
            ipaddress.ip_address(cible)
            break
        except ValueError:
            print("Addresse Ip invalide")
            cible= input("veuillez saisir une cible valide à tester: ")
            
    cmd= ["ping", "-c", "4", cible]
    reachable = False
    with subprocess.Popen(cmd,stdout= subprocess.PIPE, text=True, bufsize=1) as ping:# bufsize= 1 give output line by line 
        for lin in ping.stdout:
            if "ttl" in lin.lower():
                reachable = True
                break
    
    #Partie du scan de port       
    if reachable:
        print("machine is reachable, starting the port scanning")
        cmd= ["nmap", "-sS", cible]
        portScanning(cmd)
            
    else:
        print("machine isn't reachable")

def main():
    if os.geteuid() != 0:# geteuid pour verifier avec quel droit tu excécute ton programme
        print("Ce programme exige les droit d'excution root: veuillez saisir sudo python3 reconnaissance.py")
        return
    else:
        body()

if __name__ == '__main__':
    main()