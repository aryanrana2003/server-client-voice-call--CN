
import socket
import pyaudio
import threading

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
HOST = '192.168.157.235'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to server at", (HOST, PORT))

audio = pyaudio.PyAudio()

def send_audio():
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    while True:
        try:
            data = stream.read(CHUNK)
            client_socket.sendall(data)
        except Exception as e:
            print("Error sending data:", e)
            break
    stream.stop_stream()
    stream.close()

def receive_audio():
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
    while True:
        try:
            data = client_socket.recv(CHUNK)
            if not data:
                break
            stream.write(data)
        except Exception as e:
            print("Error receiving data:", e)
            break
    stream.stop_stream()
    stream.close()

send_thread = threading.Thread(target=send_audio)
receive_thread = threading.Thread(target=receive_audio)
send_thread.start()
receive_thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Client stopped.")
finally:
    send_thread.join()
    receive_thread.join()
    audio.terminate()
    client_socket.close()

