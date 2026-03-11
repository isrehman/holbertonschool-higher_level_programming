#!/usr/bin/python3
"""Module for client-server application with serialization"""
import socket
import json


def start_server(host='localhost', port=65432):
    """Sets up a server that receives and deserializes data"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                data += chunk
            dictionary = json.loads(data.decode('utf-8'))
            print("Received Dictionary from Client:")
            print(dictionary)


def send_data(data, host='localhost', port=65432):
    """Serializes and sends a dictionary to the server"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            serialized = json.dumps(data).encode('utf-8')
            s.sendall(serialized)
    except Exception as e:
        print("Error: {}".format(e))
