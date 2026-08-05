# 🖼️ Image Steganography App

> A lightweight, privacy-focused image steganography application built with Python and Streamlit that allows users to securely hide secret messages inside images using the Least Significant Bit (LSB) algorithm.

![Python](https://img.shields.io/badge/python-3.11-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.61.0-red)
![Pillow](https://img.shields.io/badge/pillow-latest-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

# 💡 Why This Project Exists

Traditional communication channels are often monitored, insecure, or unsuitable for transmitting sensitive information.

This project demonstrates how information can be hidden inside ordinary images without visibly changing them.

Instead of encrypting a message and making its existence obvious, steganography conceals the message itself.

The application allows users to:

- Hide secret text inside an image.
- Extract hidden messages later.
- Preserve image quality.
- Work completely offline.
- Learn the fundamentals of image steganography.

---

# 🎯 Project Goals

- Understand the concept of steganography.
- Implement the Least Significant Bit (LSB) algorithm.
- Create a user-friendly web interface using Streamlit.
- Demonstrate secure data hiding techniques.
- Build a project that can be extended with encryption and file embedding.

---

# ⭐ Key Features

## 🔐 Encode Secret Messages

Hide any text message inside an image without noticeably changing the image.

---

## 🔓 Decode Hidden Messages

Extract the hidden message from the encoded image.

---

## 🖼️ Image Preservation

The visual quality of the image remains almost identical to the original.

---

## 💻 Offline Processing

Everything runs locally on your machine.

No internet connection is required.

---

## ⚡ Streamlit Interface

Simple and interactive UI for encoding and decoding.

---

## 🧠 Educational Purpose

Understand:

- Binary representation
- Pixels
- RGB values
- Least Significant Bit manipulation
- Data encoding and decoding

---

# 🛠 Tech Stack

| Layer | Technology |
|--------|--------|
| Language | Python 3.11 |
| Frontend | Streamlit |
| Image Processing | Pillow |
| Algorithm | LSB (Least Significant Bit) |
| Environment | Virtual Environment (venv) |

---

# 🧩 How It Works

## Step 1: User uploads an image

The user uploads a PNG image.

---

## Step 2: Secret message is converted to binary

Example:

```text
HELLO

H → 01001000
E → 01000101
L → 01001100
L → 01001100
O → 01001111
```

---

## Step 3: Binary data is embedded

Each pixel consists of:

```text
(R, G, B)

Example:

(101, 220, 33)
```

Binary:

```text
101 → 01100101
220 → 11011100
33  → 00100001
```

Only the last bit is modified:

```text
01100101 → 01100100
```

The image looks the same to the human eye.

---

## Step 4: Encoded image is generated

The modified image is saved.

Example:

```text
input.png → output.png
```

---

## Step 5: Decoding

The program reads the least significant bits and reconstructs the original message.

---

# 📁 Project Structure

```text
ImageSteganography/

├── app.py
├── steganography.py
├── requirements.txt
├── README.md
│
├── images/
│   └── sample.png
│
├── output/
│   └── encoded_image.png
│
└── .venv/
```

---

# 📄 File Explanation

| File | Description |
|--------|--------|
| app.py | Streamlit UI |
| steganography.py | Encoding and decoding logic |
| requirements.txt | Project dependencies |
| README.md | Project documentation |
| images/ | Input images |
| output/ | Encoded images |

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
```

---

## 2. Move into the project folder

```bash
cd ImageSteganography
```

---

## 3. Create virtual environment

Windows:

```bash
python -m venv .venv
```

---

## 4. Activate virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

---

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run the application

```bash
streamlit run app.py
```

---

## 7. Open in browser

```text
http://localhost:8501
```

---

# 📦 Requirements

```text
streamlit
pillow
```

Install manually:

```bash
pip install streamlit pillow
```

---

# 🚀 Usage

## Encoding

1. Open the app.
2. Upload an image.
3. Enter the secret message.
4. Click Encode.
5. Download the encoded image.

---

## Decoding

1. Upload the encoded image.
2. Click Decode.
3. View the hidden message.

---

# 🔍 Algorithm Used

This project uses:

## Least Significant Bit (LSB)

The least significant bit of each pixel stores the secret data.

Example:

```text
Original:

10010110

Modified:

10010111
```

Only one bit changes.

The human eye cannot notice the difference.

---

### ⚠️ Problem Encountered During Development

While running the Streamlit application, the following error occurred:

```text
TypeError: GZipResponder.__init__() missing 1 required keyword-only argument: 'thread_minimum_size'
```

#### Cause

The issue was caused by an incompatible version of Starlette:

```text
Python 3.11.9
Streamlit 1.61.0
Starlette 1.4.0 ❌
```

Although the project was running on Python 3.11, Streamlit was using an incompatible Starlette version, which caused the application to crash during startup.

#### Solution

First, verify the installed versions:

```bash
pip show streamlit
pip show starlette
pip show uvicorn
```

If `starlette==1.4.0` is installed, uninstall it:

```bash
pip uninstall starlette -y
```

Then install a compatible version manually:

```bash
pip install "starlette>=0.47,<0.49"
```

Verify the installation:

```bash
pip show starlette
```

Finally, run the application again:

```bash
streamlit run app.py
```

#### Working Environment

```text
Python 3.11.9
Streamlit 1.61.0
Starlette 0.47.x or 0.48.x
Uvicorn 0.35.x
```

# 🧪 Future Updates

## 🔐 Password protection for decoding

Require a password before extracting hidden data.

---

## 🔒 AES encryption

Encrypt the message before embedding it inside the image.

---

## 📄 File embedding

Hide:

- PDF
- DOCX
- ZIP
- TXT
- Other files

instead of only plain text.

---

## 📊 Capacity analysis

Display:

- Maximum image capacity
- Used space
- Remaining space

---

## 🖼️ Drag-and-drop upload

Support drag-and-drop image uploading.

---

## 🌙 Light/Dark mode

Use Streamlit themes.

---

## 📜 History management

Maintain a history of encoded images.

---

## 📱 Responsive UI

Improve layout using:

- Columns
- Expanders
- Tabs
- Mobile responsiveness

---

## ☁️ Cloud deployment

Deploy online using:

- GitHub
- Streamlit Community Cloud
- Render
- Railway

---

## 🔄 Compression support

Compress messages before embedding.

---

## 🧠 AI integration

Use AI to:

- Suggest passwords
- Analyze image capacity
- Detect steganography

---

# 📚 Learning Outcomes

By building this project, you will learn:

- Image processing
- Binary representation
- Bit manipulation
- Steganography concepts
- Streamlit
- File handling
- Python packaging
- Virtual environments

---

# 📄 License

MIT License

Free to use, modify and distribute.

---

# 👨‍💻 Author

Developed with ❤️ using Python and Streamlit.