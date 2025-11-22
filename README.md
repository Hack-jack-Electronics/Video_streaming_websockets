# PC-to-PC Live Video Streaming using Python Sockets

This project demonstrates a simple and efficient method to stream live video from one computer (Sender) to another computer (Receiver) using **Python sockets**, **OpenCV**, and **Pillow**.  
It works on any Ubuntu/Linux/Windows machine with a standard laptop/webcam — no Raspberry Pi required.

---

## 🚀 Features
- Stream real-time webcam video between two PCs
- Uses raw TCP sockets (lightweight and simple)
- Works over both **LAN** and **Internet**
- Compatible with **Ubuntu**, **Windows**, **Jetson**, and more
- Low latency JPEG-based streaming
- Secure global streaming supported through **Tailscale VPN**

---

## 📦 Requirements

Install the dependencies on **both sender and receiver PCs**:

```bash
sudo apt update
sudo apt install python3-pip python3-opencv
pip install pillow numpy
```

---

## 📁 Project Structure

```
.
├── client.py   # Sender script: captures webcam frames and sends them
└── server.py   # Receiver script: receives frames and displays video
```

---

## 🖥️ Usage Instructions

### 1️⃣ Run the Receiver (server)

Find the receiver’s IP address:

```bash
hostname -I
```

Then start the server:

```bash
python3 server.py 0.0.0.0 8000
```

The server will wait for incoming video frames.

---

### 2️⃣ Run the Sender (client)

On the sender machine, run:

```bash
python3 client.py <RECEIVER_IP> 8000
```

Example:

```bash
python3 client.py 192.168.1.20 8000
```

You should now see the live video streaming on the receiver PC.

Press **Q** on the video window to stop streaming.

---

## 🌍 Streaming Over the Internet (Different Networks)

To stream across completely different networks safely, use **Tailscale**.

### Install Tailscale on both machines:
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

Get the receiver’s Tailscale IP:

```bash
tailscale ip -4
```

Example:
```
100.105.22.18
```

Use this IP in the client command:

Sender:
```bash
python3 client.py 100.105.22.18 8000
```

Receiver:
```bash
python3 server.py 0.0.0.0 8000
```

You can now stream video securely **from anywhere in the world**.

---

## 📊 Performance

| Network Type | Latency | FPS (Approx.) |
|--------------|---------|----------------|
| LAN | 10–40 ms | 15–25 FPS |
| Tailscale (Internet) | 80–200 ms | 10–18 FPS |
| Jetson Nano Sender | Lower latency | Higher FPS |

---

## 🔧 Troubleshooting

### ❌ Connection Refused
- Server not running
- Wrong IP address
- Firewall/port blocking

### ❌ Black Screen
- Camera busy: try a different index
  ```python
  cv2.VideoCapture(1)
  ```

### ❌ Lag or Low FPS
Lower resolution:
```python
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
```

---

## 🛠️ Future Enhancements
- Add audio streaming
- Add authentication/password
- Add support for multiple clients
- Add GUI for control
- Use UDP for ultra-low latency
- Add H.264 compression

---

## 📄 License
This project is open-source under the **MIT License**.  
You are free to use, distribute, and modify it.

---

## 🙌 Author
Created by Tanishk Singhal  
If you like this project, consider giving it a ⭐ on GitHub!

