import os
import secrets

ENV_FILE = ".env"
SECRET_KEY_NAME = "DJANGO_SECRET_KEY"

def generate_secret_key():
    return secrets.token_urlsafe(50)

def save_to_env_file(secret_key):
    lines = []

    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as f:
            lines = f.readlines()

    found = False
    for i, line in enumerate(lines):
        if line.startswith(f"{SECRET_KEY_NAME}="):
            lines[i] = f"{SECRET_KEY_NAME}={secret_key}\n"
            found = True
            break

    if not found:
        lines.append(f"{SECRET_KEY_NAME}={secret_key}\n")

    with open(ENV_FILE, "w") as f:
        f.writelines(lines)

    print(f"Clave secreta guardada en {ENV_FILE} como {SECRET_KEY_NAME}.")

if __name__ == "__main__":
    key = generate_secret_key()
    save_to_env_file(key)

