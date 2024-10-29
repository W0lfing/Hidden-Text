def ip_to_text(ip_addresses):
    # Convert IP-like addresses to text
    text = ""
    for ip in ip_addresses:
        # Split the IP address into its octets
        octets = ip.split('.')
        # Convert each octet to its corresponding character
        for octet in octets:
            char = chr(int(octet))  # Convert decimal to character
            text += char
    return text

if __name__ == "__main__":
    # Prompt the user to input IP-like addresses
    ip_addresses = []
    print("Enter IP-like addresses (enter 'done' to finish):")
    while True:
        ip = input()
        if ip.lower() == 'done':
            break
        ip_addresses.append(ip)

    # Decrypting the IP-like addresses
    decrypted_text = ip_to_text(ip_addresses)
    
    # Print the decrypted text
    print(f"Decrypted text: {decrypted_text}")
