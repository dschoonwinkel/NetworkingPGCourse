import socket

import pypacker.pypacker as pypacker
from pypacker.pypacker import Packet
from pypacker import psocket
from pypacker.layer12 import arp, ethernet, ieee80211, prism
from pypacker.layer3 import ip, icmp

psock = psocket.SocketHndl(iface_name="lo0", mode=psocket.SocketHndl.MODE_LAYER_2, timeout=10)

# send ARP request
arpreq = ethernet.Ethernet(src_s="12:34:56:78:90:12", type=ethernet.ETH_TYPE_ARP) +\
    arp.ARP(sha_s="12:34:56:78:90:12", spa_s="192.168.0.2",
        tha_s="12:34:56:78:90:13", tpa_s="192.168.0.1")
psock.send(arpreq.bin())

# send ICMP request
icmpreq = ethernet.Ethernet(src_s="12:34:56:78:90:12", dst_s="12:34:56:78:90:13", type=ethernet.ETH_TYPE_IP) +\
    ip.IP(p=ip.IP_PROTO_ICMP, src_s="192.168.0.2", dst_s="192.168.0.1") +\
    icmp.ICMP(type=8) +\
    icmp.ICMP.Echo(id=1, ts=123456789, body_bytes=b"12345678901234567890")
psock.send(icmpreq.bin())