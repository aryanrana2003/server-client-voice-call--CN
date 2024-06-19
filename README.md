# Audio Streaming Client-Server Application

This repository contains a simple client-server application for streaming audio over a network using Python. The client and server communicate using TCP/IP sockets and handle audio streaming using the `pyaudio` library.

## Prerequisites

To run this application, you need:

- Python 3.x
- `pyaudio` library (`pip install pyaudio`)

## Components

### Client (`client.py`)

The client script (`client.py`) connects to a server and streams audio input to the server while simultaneously receiving audio data from the server and playing it back.

#### Configuration

- Edit `client.py` to set the correct `HOST` IP address to match your server's IP address.
- Adjust other parameters like `FORMAT`, `CHANNELS`, `RATE`, and `CHUNK` based on your audio requirements.

#### Usage

1. **Start the Client:**

   - Run `python client.py` to start the client.
   - The client will attempt to connect to the server specified by `HOST` and `PORT`.

2. **Audio Streaming:**

   - The client continuously captures audio from the microphone using `pyaudio`.
   - Audio data is encoded and sent to the server in chunks (`CHUNK` size).
   - Simultaneously, the client receives audio data from the server and plays it back in real-time.

3. **Termination:**

   - Use `Ctrl + C` to stop the client.
   - This will terminate the audio streaming threads, close the socket connection, and release audio resources.

### Server (`server.py`)

The server script (`server.py`) listens for incoming client connections. It manages multiple clients concurrently, broadcasting received audio data to all connected clients.

#### Configuration

- By default, the server listens on port `12345`. Change `PORT` if needed.
- Ensure the server has permissions to bind to the chosen port, especially on restricted environments like cloud servers.

#### Usage

1. **Start the Server:**

   - Run `python server.py` to start the server.
   - The server will start listening for incoming client connections.

2. **Handling Clients:**

   - Upon connection, the server prompts clients to choose a nickname (`NICK`).
   - Clients can then send and receive audio data to/from the server and other connected clients.

3. **Broadcasting Audio:**

   - The server receives audio data from one client and broadcasts it to all other connected clients.
   - Audio playback is synchronized across all clients receiving the broadcast.

4. **Termination:**

   - Use `Ctrl + C` to stop the server.
   - This gracefully terminates all client connections, closes sockets, and releases resources.

## Troubleshooting

- **Connection Issues:**
  - Ensure both client and server are on the same network if testing locally.
  - Check firewall settings to allow TCP traffic on the specified port (`12345` by default).

- **Audio Quality:**
  - Adjust `RATE` and `CHUNK` size in both client and server scripts to optimize audio quality and latency.
  - Consider using compression techniques or different audio formats (`FORMAT`) based on network conditions.

- **Resource Management:**
  - Monitor CPU and memory usage, especially when scaling up the number of clients.
  - Use threading and socket timeouts to handle disconnects and idle clients efficiently.

## Future Enhancements

- **Encryption and Security:**
  - Implement SSL/TLS for secure communication between client and server.
  - Encrypt audio data to protect privacy and prevent unauthorized acc  ess.

- **GUI Integration:**
  - Develop a graphical user interface (GUI) for both client and server applications.
  - Include controls for audio input/output settings and visual feedback during streaming.

- **Additional Features:**
  - Integrate audio recording and playback controls.
  - Support for multiple audio channels or simultaneous audio streams.

## Additional Resources

- [Python Documentation](https://www.python.org/doc/)
- [PyAudio Documentation](https://people.csail.mit.edu/hubert/pyaudio/docs/)
- [Socket Programming in Python](https://realpython.com/python-sockets/)
- [Markdown Guide](https://www.markdownguide.org/)

Feel free to contribute, modify, or adapt this application for your specific use case or environment. Happy coding!
