from colorama import Back , Fore , Style , init

init(autoreset=True)
print(Back.GREEN  + "Access Granted")
print(Style.DIM + "Denied")
print(Style.BRIGHT + "Granted")
print(Style.NORMAL + "entry point")
print(Fore.RED + "entry point")

