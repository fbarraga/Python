# Instal·lació de Python3 

Python és un llenguage multiplataforma, per lo que el mateix programa ens pot funcionar en Linux, Windows i MacOs. La pàgina principal para descarregar les diferents versions és: [www.python.org/downloads/](https://www.python.org/downloads/).

## Instal·lació en Linux

Python ve preinstal·lat de sèrie en la majoria de las distribucions GNU/Linux. Si no el trobem instal·lat sempre el podrem instal·lar a través dels paquets de instal·lació.

* Amb Debian 11.3 , la versió es la 3.10.6
* Amb Ubuntu 22.04 , la versió es la 3.10.6

[Per més informació](https://docs.python.org/3/using/unix.html)

## Instal·lació en Windows

Podem descarregar-nos un instal·lador (paquet MSI) de les diferents versions de Python. 

[Per més informació](https://docs.python.org/3/using/windows.html)

Amb Windows hem de desactivar la seguretat en l'execució d'scripts, sino Python ens donarà error. Després d'instal·lar-ho des de Powershell i amb permissos d'administrador executem:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```


## Instal·lació en Mac OS

Mac OS X 10.8 ve amb Python 2.7 pre-instal·lat. Si vols instal·lar Python3 pots trobar el paquet de la versió desitjada a la pàgina de descàrrega: [www.python.org/downloads/](https://www.python.org/downloads/).

[Per més informació](https://docs.python.org/3/using/mac.html)


***
[Index](../../../README.md)
