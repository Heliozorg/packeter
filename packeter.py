import socket
import keyboard  # type: ignore
import time

# Get UDP and TCP port numbers from user input

udp_port = int(input("Enter UDP destination port: "))
tcp_port = int(input("Enter TCP destination port: "))

# Get UDP and TCP messages from user input
udp_text = input("Enter UDP message: ")
tcp_text = input("Enter TCP message: ")

# Encode the messages to bytes
udpb = udp_text.encode('utf-8')
tcpb = tcp_text.encode('utf-8')

# Define addresses
UDP_ADDRESS = (("8.8.8.8"), udp_port) # Replace with real ip
TCP_ADDRESS = (("8.8.8.8"), tcp_port) # Same here

# Create a UDP socket
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create a TCP socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect the TCP socket to the server
    tcp_sock.connect(TCP_ADDRESS)

    # Fat silly loop
    while True:
        try:
            if keyboard.is_pressed('q'):
                break
            
            # Send a UDP packet
            udp_sock.sendto(udpb, UDP_ADDRESS)
            print("Packet sent on UDP port:", UDP_ADDRESS)

            # Send a TCP packet
            tcp_sock.send(tcpb)
            print("Packet sent on TCP port:", TCP_ADDRESS)

            # Optional: Add a small delay to prevent flooding
            # time.sleep(10)

        except KeyboardInterrupt:
            # Handle the case where 'q' is pressed during execution
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the sockets
    udp_sock.close()
    tcp_sock.close()
