def text_to_binary(text):
    # Convert each character to its ASCII value and then to binary
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_ip(binary_string):
    # Ensure the binary string length is a multiple of 32, pad if necessary
    while len(binary_string) % 32 != 0:
        binary_string += '0'
    
    ip_addresses = []
    
    # Split binary string into 32-bit chunks
    for i in range(0, len(binary_string), 32):
        chunk = binary_string[i:i+32]
        # Split into 4 octets (8 bits each)
        octets = [chunk[j:j+8] for j in range(0, 32, 8)]
        # Convert each 8-bit chunk to decimal
        ip_octets = [str(int(octet, 2)) for octet in octets]
        # Form an IP-like address
        ip_address = '.'.join(ip_octets)
        ip_addresses.append(ip_address)
    
    return ip_addresses

def encrypt_to_ip(sentence):
    binary_sentence = text_to_binary(sentence)
    ip_format_list = binary_to_ip(binary_sentence)
    return ip_format_list

# Main program
if __name__ == "__main__":
    # Ask the user to input a sentence
    sentence = input("Enter the sentence you want to encrypt: ")
    
    # Encrypt the sentence and get the IP-like addresses
    encrypted_ips = encrypt_to_ip(sentence)
    
    # Print the resulting IP-like addresses
    print("\nEncrypted IP-like addresses:")
    for ip in encrypted_ips:
        print(ip)
