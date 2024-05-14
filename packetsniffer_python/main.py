import socket 
import textwrap 
 
def main():
     conn = socket.socket(SOCKET.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) 

     while True: 
         raw_data, addr = conn.recvfrom(65535) #Biggest buffer size you can have
         dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
         print('\n Ethernet Frame: ')
         print('Destinaton {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))






# First, I am going to unpack the ethernet frame 

 # this is mainly for the byte conversion
 # Handled by socket -> Little indian byte format 


def unpack_ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14]) # receiver = 6bytes, sender = 6bytes, type = 2bytes
    return get_mac_adress(dest_mac), get_mac_adress(src_mac), socket.htons (proto), data[14:]
    
  
# Now i will format mac Adress (Human readable / standard convention / 2 decimal places seprated by colon)
# Conventional Mac Adress -> (AA:BB:CC:DD:EE:FF)

def get_mac_adress(bytes_adress): 
    bytes_str = map('{:02x}'.format, bytes_adress)
    mac_adress = ':'.join(bytes_str).upper()
    return mac_adress


# unpack IPv4 packet 

def ipv4_packet(data): # shifting right 4 bits
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]


# return properyl formattefd ipv4 adress

def ipv4(addr):
    return '.'.join(map(str,addr))

# Using mainly TPC protocols


# but first check if ICMP packet valid 
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('!, B, B, H', data[:4])
    return icmp_type, code, checksum, data[4:]

# now unpacking the TCP 

def tcp_segment(data):
    (src_port, dest_port, sequence, achknowledgment, offset,reserved_flags) = 
    struct.unpack ('! H H L L H ', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, achknowledgment, 
    flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin , data [offset:]

#unapcking UDP now

def udp_segment(data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', data[:8])
    return src_port, dest_port, size, data[8:]

# Format Multiline data
def format_multi_line(prefix,string, size = 80):
    size = len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size = 1 
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

main()


    
