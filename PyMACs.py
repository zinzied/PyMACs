from Banner import banner
import random
from colorama import Fore, Style, init

init(autoreset=True)  # Enable colorama for Windows

print(banner())

def generate_mac_addresses(num_macs):
    count = 0
    while count < num_macs:
        mac = '00:1A:79:' + ':'.join(f'{random.randint(0, 255):02X}' for _ in range(3))
        yield mac
        count += 1

# Ask the user how many MAC addresses they want to generate
num_macs_to_generate = int(input("Enter the number of MAC addresses to generate: "))

# Generate the MAC addresses
mac_addresses = []
for mac in generate_mac_addresses(num_macs_to_generate):
    mac_addresses.append(mac)

# Save the generated MAC addresses to a text file
with open('generated.txt', 'w') as file:
    for mac in mac_addresses:
        file.write(mac + '\n')

# Print thank you message with colors
print(Fore.GREEN + "Addresses MAC Generated!" + Style.RESET_ALL)
print(Fore.GREEN + "Thank you for using my app!" + Style.RESET_ALL)
print(Fore.CYAN + "CYA" + Style.RESET_ALL)

input("Press any key to exit...")