import socket

def process_message(message):
    if message == "Ciclo normal" or message == "Ciclo normalCiclo normal" or message == "Ciclo normalCiclo normalCiclo normalCiclo normal":
        return "Lavado estandar con agua tibia"
    elif message == "Ciclo rapido" or message == "Ciclo rapidoCiclo rapido" or message == "Ciclo rapidoCiclo rapidoCiclo rapido" or message == "Ciclo rapidoCiclo rapidoCiclo rapidoCiclo rapido":
        return "Lavado corto conagua fria"
    elif message == "Ropa d color" or message == "Ropa d colorRopa d color" or message == "Ropa d colorRopa d colorRopa d color" or message == "Ropa d colorRopa d colorRopa d colorRopa d color":
        return "Recomendado paraproteger colores"
    elif message == "Ropa blanca " or message == "Ropa blanca Ropa blanca " or message == "Ropa blanca Ropa blanca Ropa blanca " or message == "Ropa blanca Ropa blanca Ropa blanca Ropa blanca ": 
        return "Lavado caliente para eliminar   manchas"
    elif message == "Delicados   " or message == "Delicados   Delicados   " or message == "Delicados   Delicados   Delicados   " or message == "Delicados   Delicados   Delicados   Delicados   ":
        return "Lavado suave conagua fria"
    elif message == "Carga pesada" or message == "Carga pesadaCarga pesada" or message == "Carga pesadaCarga pesadaCarga pesada" or message == "Carga pesadaCarga pesadaCarga pesadaCarga pesada":
        return "Lavado intenso  de agua caliente"
    else:
        return "Ciclo no reconocido"

def start_server():
    host = '192.168.1.65'  # Cambia esto a la IP de tu servidor
    port = 12345  # Escoge un puerto disponible

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Escucha una conexión entrante

    print(f"Server is listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            data = client_socket.recv(1024).decode()
            print(f"Received message: {data}")
            response = process_message(data)
            client_socket.send(response.encode())
        except Exception as e:
            print(f"Error sending data: {e}")
        finally:
            client_socket.close()
            print(f"Connection closed with {client_address}")

if __name__ == "__main__":
    start_server()
