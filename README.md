# 🔐 Hash Cracker CLI Tool

## 📌 Description
Hash Cracker is a simple and efficient command-line tool for detecting hash types and cracking hashes using a wordlist. It supports multiple hash algorithms like **MD5, SHA1, SHA224, SHA256, SHA384, and SHA512**.

## 🚀 Features
- 🔍 **Automatic Hash Type Detection**
- 🔑 **Wordlist-Based Hash Cracking**
- 🎨 **Colorized Output for Better Readability**
- ⏳ **ASCII Loading Animation for Enhanced UX**
- 💻 **Lightweight & Easy to Use**

## 📥 Installation
Ensure you have Python installed (>=3.x). Then, clone the repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/yourusername/hash-cracker.git
cd hash-cracker

# Install required packages
pip install -r requirements.txt
```

## 🔧 Usage
Run the tool from the command line:

```bash
python hcrack.py <hash_value> <wordlist_file>
```

### Example:
```bash
python hcrack.py 5d41402abc4b2a76b9719d911017c592 wordlist.txt
```
*(The hash above corresponds to "hello" in MD5)*

## 📜 Supported Hashes
| Hash Type | Length |
|-----------|--------|
| MD5       | 32     |
| SHA1      | 40     |
| SHA224    | 56     |
| SHA256    | 64     |
| SHA384    | 96     |
| SHA512    | 128    |

## 🖥️ Example Output
```
Detected Hash Type: MD5
Cracking hash... /
Cracking hash... -
Cracking hash... \
✅ Match Found! Password: hello
```
If no match is found:
```
❌ Matching failed.
```

## 🛠️ Future Improvements
- Multi-threading for faster cracking 🔥
- Custom hash type detection ⚡
- Online API integration for cracking 💻

## 📜 License
This project is open-source and available under the MIT License.

## 💬 Contact
For support or contributions, reach out at **advent007@duck.com**.

