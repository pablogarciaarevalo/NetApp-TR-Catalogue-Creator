# NetApp-TR-Catalogue-Creator
Create a NetApp Technical Report Catalogue

## Getting Started

This script index the NetApp Technical Reports which has been published and create a catalogue with html format for submit at [https://pablogarciaarevalo.com/NetApp_TR_Catalogue.html](https://pablogarciaarevalo.com/NetApp_TR_Catalogue.html)

## Requirements

The below python libraries are required

```
pip3 install lxml
pip3 install requests
pip3 install pdfrw
```

## Running

Example running the script with an output with several public documents
```
> python TR-catalogue-creator.py
<a href="http://www.netapp.com/us/media/tr-3001.pdf" class="TR-url" target="_blank">TR-3001: A Storage Networking Appliance</a><br />
<a href="http://www.netapp.com/us/media/tr-3009.pdf" class="TR-url" target="_blank">TR-3009: Filer Deployment Strategies for Evolving LAN Topologies</a><br />
```
