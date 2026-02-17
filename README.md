# 🛡️ PoC: STP-CLAIM-ROOT

![Status](https://img.shields.io/badge/Estado-Finalizado-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Scapy](https://img.shields.io/badge/Library-Scapy-yellow)

## 📋 Descripción Técnica
Este repositorio contiene una Prueba de Concepto (PoC) desarrollada en Python utilizando el framework **Scapy**. 

## Objetivo del script:

Forzar un recálculo de la topología de red inyectando BPDUs (Bridge Protocol Data Units) superiores con una prioridad de puente (Bridge Priority) de 0. Esto obliga a los switches a elegir la máquina del atacante como el "Root Bridge", permitiendo la intercepción de tráfico y causando inestabilidad en la red.

El script demuestra vulnerabilidades críticas en la Capa 2 (Enlace de Datos) del modelo OSI, permitiendo auditar la seguridad de la infraestructura de red conmutada.

## 🗺️ Topología y Escenario

El entorno de pruebas fue desplegado utilizando **GNS3** con emulación de hardware Cisco (IOU) y máquinas virtuales atacantes.

| Dispositivo | Rol | IP / Interfaz | Detalles |
| :--- | :--- | :--- | :--- |
| **Kali Linux** | Atacante | `10.14.14.6` / `eth1` | Origen de la inyección de paquetes. |
| **Cisco IOU L3** | Gateway (Víctima) | `10.14.14.1` / `e0/1` | Router/Switch de borde. |
| **Cisco IOU L2** | Switch de Acceso | N/A (Capa 2) | Dispositivo donde se inyecta tráfico. |
| **VLAN** | Segmento | VLAN 1 (Nativa) | Red `10.14.14.0/24`. |

### Diagrama Lógico
<img width="386" height="379" alt="image" src="https://github.com/user-attachments/assets/e9af0119-b0fd-4958-bc13-71c6cbcc14a5" />



## ⚙️ Requisitos y Dependencias

Para ejecutar esta herramienta se requiere:
* **Sistema Operativo:** Linux (Kali Linux, Parrot OS, Ubuntu).
* **Python:** Versión 3.8 o superior.
* **Permisos:** Acceso **Root** (sudo) es mandatorio para la manipulación de sockets raw.
* **Librerías:**
    ```bash
    pip install scapy
    ```

## 🚀 Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone (https://github.com/chris-dlsb/STP-CLAIM-ROOT.git)
    cd STP-CLAIM-ROOT
    ```

2.  **Ejecutar el script:**
    ```bash
    sudo python3 STP-CLAIM-ROOT.py
    ```

### Parámetros Configurados
* **Interfaz:** `eth1` (Hardcoded o por argumento, según tu script).
* **Target:** Broadcast `ff:ff:ff:ff:ff:ff` o Multicast STP `01:80:c2:00:00:00`.

## 📸 Evidencia de Funcionamiento (PoC)

**1. Ejecución del Ataque:**
<img width="864" height="117" alt="image" src="https://github.com/user-attachments/assets/4a5009ff-b77f-4af9-9a30-7aeef16953f5" />


**3. Impacto en la Víctima:**
<img width="731" height="253" alt="image" src="https://github.com/user-attachments/assets/2ef4e6fb-29ef-4676-b3e9-33397fb0e2e0" />

## 🛡️ Medidas de Mitigación

Para proteger la infraestructura contra este vector de ataque, se recomienda implementar:

[MITIGACIONES ESPECÍFICAS]:

Root Guard: Configurar spanning-tree guard root en los puertos de acceso para evitar que dispositivos no autorizados se conviertan en Root Bridge.

BPDU Guard: Habilitar spanning-tree bpduguard enable en puertos configurados con PortFast. Si se recibe un BPDU en estos puertos, la interfaz se apagará automáticamente (err-disable)

---
*Descargo de Responsabilidad: Este software fue creado únicamente con fines académicos. El autor no se hace responsable del mal uso de esta herramienta.*

**Autor:** Cristopher De Los Santos  
**Matrícula:** 2024-1414
