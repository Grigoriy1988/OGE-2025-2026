from ipaddress import *

ip = "178.32.174.234"
mask = '255.255.248.0'
net = ip_network(f'{ip}/{mask}',0)
ip2 = '178.32.174.8'
ip3 = '178.32.175.102'
ip4 = '178.32.2.234'
ip5 = '178.32.174.234'
ip6 = '213.32.174.234'
ip7 = '213.174.32.178'
net2 = ip_network(f'{ip2}/{mask}',0)
net3 = ip_network(f'{ip3}/{mask}',0)
net4 = ip_network(f'{ip4}/{mask}',0)
net5 = ip_network(f'{ip5}/{mask}',0)
net6 = ip_network(f'{ip6}/{mask}',0)
net7 = ip_network(f'{ip7}/{mask}',0)
print(net==net6)