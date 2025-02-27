from requests import get
import os
import threading
from colorama import Fore, init
import time
import sys

os.system('clear')
init(autoreset=True)

# Define lists
list_pasvand = [
    'creator', 'maker', 'lockader', 'makerby', 'malik', 'omnific', 'Team', 'GP',
    'info', 'official', 'The', 'BBC', 'Group', 'leader', 'Guard', 'Lord', 'Malek',
    'ekip', 'original', 'Owner', 'Khaleq', 'Bax', 'The_Creator', 'FcCreator',
    'createby', 'create', 'my'
]

list_hoveiat = [
    'afi', 'mr', 'malake', 'malakeh', 'master', 'mester',
    'peranses', 'amir', 'ati', 'fati', 'kiana', 'pir', 'pedar', 'pedar_bozorg',
    'pedarbozorg', 'arosak', 'arocak', 'taha', 'shayan', 'sara', 'seti',
    'shah', 'padeshah', 'teymor', 'aria', 'arian', 'aros', 'ema', 'emi',
    'ermia', 'ehsan', 'mahta', 'mahtab', 'ronal', 'khan', 'koloft', 'roya',
    'soheil', 'sohil', 'rafi', 'ralfi', 'delvin', 'ana', 'melisa', 'pari',
    'erfan', 'saman', 'sina', 'ostoreh', 'efi', 'ayda', 'pariya', 'parisa',
    'paniz', 'jeneral', 'armita', 'anita', 'farmanrava', 'farmandeh', 'arash',
    'hakem', 'sepehr', 'yas', 'yasaman', 'hosein', 'hossien', 'shahdokht',
    'sami', 'samyar', 'ghazi', 'janan', 'meysam', 'arsalan', 'sajad', 'helma',
    'rozhan', 'dorsa', 'saleh', 'mina', 'mona', 'deli', 'sarina',
    'doki', 'doctor', 'doktor', 'bozorg', 'mamad', 'mmd', 'lat', 'thomas',
    'raha', 'ghazal', 'elizabet', 'shaddokht', 'bita', 'eli', 'Sinderla',
    'barbi', 'mehrab', 'emperrator', 'Shahanshah', 'hamid', 'reza', 'mehdi',
    'ali', 'afshar', 'doshizeh', 'bano', 'arta', 'kavian', 'kamran', 'amo',
    'milad', 'mojtaba', 'leo', 'sinderela', 'sinderella', 'behnam', 'atena',
    'khaton', 'gonde', 'gondeh', 'gondeh_lat', 'gonde_lat', 'gondehlat',
    'gondelat', 'shazde', 'shazdeh', 'sadra', 'sogand', 'yalda', 'arman',
    'abol', 'daniel', 'richard', 'mati', 'hazrat', 'alahazrat', 'lady',
    'ladi', 'Mader', 'Lat', 'Dark', 'Mohi', 'Pyr', 'Tony', 'Sheitan', 'Tina',
    'Feri', 'Meli', 'Sarhang', 'Sarbaz', 'Dani', 'Malek', 'Sardar', 'Bano',
    'Emam', 'Mohammad', 'Mohammed', 'Mohamad', 'Mamd', 'saeed', 'armin',
    'Arash', 'Kian', 'Nima', 'Sima', 'Tara', 'Darya', 'Shayan',
    'Setareh', 'Fatima', 'Hassan', 'Hussein', 'Zainab', 'Omar', 'Aisha',
    'Ibrahim', 'Khalid', 'Yasir', 'Layla', 'Rami', 'Samir', 'Nour', 'Bilal',
    'Jamil', 'Salma', 'Tariq'
]

# Menu for user to choose
print("Select an option:")
print("1. Run without list_pasvand")
print("2. Run without list_hoveiat")
print("3. Check {tag} + {list_hoveiat}")
print("4. Run with both lists in the format {list_pasvand}_{list_hoveiat}_{tag}")
print("5. Check All in order: 1, 2, 3, 4")

# Get user choice
choice = input("Enter your choice (1, 2, 3, 4, or 5): ").strip()

# Get tag input from user
tags_input = input("Please enter tags separated by spaces: ")
tags = tags_input.split()  # Split the input into a list of tags

# Calculate estimated time and internet usage
if choice == '1':
    total_combinations = len(list_hoveiat) * len(tags)  # Only for option 1
elif choice == '2':
    total_combinations = len(list_pasvand) * len(tags)  # Only for option 2
elif choice == '3':
    total_combinations = len(list_hoveiat) * len(tags)  # Only for option 3
elif choice == '4':
    total_combinations = len(list_pasvand) * len(list_hoveiat) * len(tags)  # Option 4
elif choice == '5':
    total_combinations = (len(list_pasvand) * len(tags)) + (len(list_hoveiat) * len(tags)) + (len(list_pasvand) * len(list_hoveiat) * len(tags))  # All combinations
else:
    print(Fore.RED + "Invalid choice. Exiting.")
    sys.exit()

# Calculate estimated internet usage (in KB)
estimated_internet_usage_kb = total_combinations * 1  # Assuming 1 KB per request
estimated_internet_usage_mb = estimated_internet_usage_kb / 1024  # Convert to MB

# Display estimated time and internet usage
if total_combinations > 0:
    estimated_time_seconds = total_combinations  # Assuming 1 second per request
    estimated_time_minutes = estimated_time_seconds // 60
    estimated_time_hours = estimated_time_minutes // 60
    estimated_time_seconds = estimated_time_seconds % 60
    estimated_time_minutes = estimated_time_minutes % 60
    print(Fore.YELLOW + f"Estimated time to find channels: {estimated_time_hours} hours, {estimated_time_minutes} minutes, and {estimated_time_seconds} seconds.")
    print(Fore.YELLOW + f"Estimated internet usage: {estimated_internet_usage_kb:.2f} KB ({estimated_internet_usage_mb:.2f} MB).")
else:
    print(Fore.YELLOW + "No combinations to check.")

# Ask user if they want to continue
continue_choice = input("Do you want to continue? (y/n): ").strip().lower()
if continue_choice != 'y':
    print(Fore.RED + "Exiting the program.")
    sys.exit()

# Clear the terminal screen
os.system('clear')

# List to store found channels
found_channels = []

# Function to check connection status
def check_connection():
    url = 'https://rubika.ir/rubika'
    while True:
        try:
            response = get(url)
            content = response.content.decode()

            # Check for the presence of the word "کانال" in the response
            if 'کانال' in content:
                print(Fore.YELLOW + "Connection established")
            else:
                print(Fore.RED + "Connection lost")

        except Exception as e:
            print(Fore.RED + "Error in request: " + str(e))

        time.sleep(30)  # Wait for 30 seconds before the next request

# Start checking connection in a separate thread
connection_thread = threading.Thread(target=check_connection)
connection_thread.daemon = True
connection_thread.start()

# Function to check channels based on the selected option
def check_channels(search_pasvand, search_hoveiat):
    if search_pasvand:  # If there are creators
        for creator in search_pasvand:
            for tag in tags:
                # Construct URL
                X = f'https://rubika.ir/{creator}_{tag}'
                try:
                    # Send request to URL
                    response = get(X)
                    l = response.content.decode()

                    # Check for the presence of the word "کانال" in the response
                    if 'کانال' in l:
                        channel_link = X.replace('https://rubika.ir/', '@')
                        print(Fore.GREEN + f"{channel_link} - کانال وجود دارد")
                        found_channels.append(channel_link)
                    else:
                        print(Fore.RED + f"{X} - کانال وجود ندارد")

                except Exception as e:
                    print(Fore.RED + f"Error in request: {e}")

    if search_hoveiat:  # If there are hoveiat
        for hoveiat in search_hoveiat:
            for tag in tags:
                # Construct URL without creator
                X = f'https://rubika.ir/{hoveiat}_{tag}'
                try:
                    # Send request to URL
                    response = get(X)
                    l = response.content.decode()

                    # Check for the presence of the word "کانال" in the response
                    if 'کانال' in l:
                        channel_link = X.replace('https://rubika.ir/', '@')
                        print(Fore.GREEN + f"{channel_link} - کانال وجود دارد")
                        found_channels.append(channel_link)
                    else:
                        print(Fore.RED + f"{X} - کانال وجود ندارد")

                except Exception as e:
                    print(Fore.RED + f"Error in request: {e}")

# Check based on user choice
if choice == '1':
    check_channels([], list_hoveiat)  # Run without list_pasvand
elif choice == '2':
    check_channels(list_pasvand, [])  # Run without list_hoveiat
elif choice == '3':
    for hoveiat in list_hoveiat:
        for tag in tags:
            # Construct URL
            X = f'https://rubika.ir/{tag}_{hoveiat}'
            try:
                # Send request to URL
                response = get(X)
                l = response.content.decode()

                # Check for the presence of the word "کانال" in the response
                if 'کانال' in l:
                    channel_link = X.replace('https://rubika.ir/', '@')
                    print(Fore.GREEN + f"{channel_link} - کانال وجود دارد")
                    found_channels.append(channel_link)
                else:
                    print(Fore.RED + f"{X} - کانال وجود ندارد")

            except Exception as e:
                print(Fore.RED + f"Error in request: {e}")

elif choice == '4':
    for creator in list_pasvand:  # Option 4
        for hoveiat in list_hoveiat:
            for tag in tags:
                # Construct URL
                X = f'https://rubika.ir/{creator}_{hoveiat}_{tag}'
                try:
                    # Send request to URL
                    response = get(X)
                    l = response.content.decode()

                    # Check for the presence of the word "کانال" in the response
                    if 'کانال' in l:
                        channel_link = X.replace('https://rubika.ir/', '@')
                        print(Fore.GREEN + f"{channel_link} - کانال وجود دارد")
                        found_channels.append(channel_link)
                    else:
                        print(Fore.RED + f"{X} - کانال وجود ندارد")

                except Exception as e:
                    print(Fore.RED + f"Error in request: {e}")

elif choice == '5':
    # Check all combinations in order: 1, 2, 3, 4
    check_channels([], list_hoveiat)  # Option 1
    check_channels(list_pasvand, [])  # Option 2
    for hoveiat in list_hoveiat:  # Option 3
        for tag in tags:
            # Construct URL
            X = f'https://rubika.ir/{tag}_{hoveiat}'
            try:
                # Send request to URL
                response = get(X)
                l = response.content.decode()

                # Check for the presence of the word "کانال" in the response
                if 'کانال' in l:
                    channel_link = X.replace('https://rubika.ir/', '@')
                    print(Fore.GREEN + f"{channel_link} - کانال وجود دارد")
                    found_channels.append(channel_link)
                else:
                    print(Fore.RED + f"{X} - کانال وجود ندارد")

            except Exception as e:
                print(Fore.RED + f"Error in request: {e}")

    for creator in list_pasvand:  # Option 4
        for hoveiat in list_hoveiat:
            for tag in tags:
                # Construct URL
                X = f'https://rubika.ir/{creator}_{hoveiat}_{tag}'
                try:
                    # Send request to URL
                    response = get(X)
                    l = response.content.decode()

                    # Check for the presence of the word "کانال" in the response
                    if 'کانال' in l:
                        channel_link = X.replace('https://rubika.ir/', '@')
                        print(Fore.GREEN + f"{channel_link} - کانال وجود دارد")
                        found_channels.append(channel_link)
                    else:
                        print(Fore.RED + f"{X} - کانال وجود ندارد")

                except Exception as e:
                    print(Fore.RED + f"Error in request: {e}")

# Clear the terminal screen again
os.system('clear')

# Print all found channels in green with numbers
print(Fore.GREEN + "\nFound Channels:")
for index, channel in enumerate(found_channels, start=1):
    print(f"{index}. {channel}")

# Exit the program after processing
sys.exit()
