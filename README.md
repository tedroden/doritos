# 🤖 Doritos! 

## 🚀 Introduction

Welcome to the **just talking to Doritos** project! The goal of this project is to:

1. 🏆 **Build a helpful assistant** that outperforms "OK Google"
2. 👨‍👩‍👧 **Collaborate with my kids** on writing the code

This is a fun and educational journey to explore voice recognition and artificial intelligence. Let's dive in! 🌊

### "i was talking to Doritos"

![I just want to talk to doritos](lore/doritos.png)

Years ago, Doritos (the triangular chip company) had a promotion where they had pride colored corn chips. The Facebook comments were amazing and this lady "talking to doritos" has lived in my head ever since. 

In this case, Doritos is a great `wake word`, a fine snack, and a flagrant brand appropriation.


## Running it

Get yourself a good microphone and plug it into your computer. We've been using an [old USB conference calling microphone](https://amzn.to/4cmx65Z).

You need an `OPENAI_API_KEY` in your environment. I suggest using [`pass`](https://www.passwordstore.org/) and setting it then running this like so:

``` shell
OPENAI_API_KEY=`pass OPENAI_API_KEY` python src/main.py`
```

Then, using your mouth or similar, say something like:

 - "Doritos, what time is it?" 
 - "Hey doritos, what is the first line of the great gatsby?"
 - "Yo doritos, what is Kevin Durant's instragram name?"

## 🛠️ Dev Setup

### 📋 Pre-requisites

Before you begin, ensure you have met the following requirements:

1. **Operating System**: macOS or Debian-esque Linux
2. **Python**: Version 3.6 or above

### 🍎 macOS Setup

First, you'll need to install `portaudio`:

```shell
brew install portaudio
```

### 🐧 Debian-esque Linux Setup

For Debian-based systems, install `python-pyaudio`:

```shell
sudo apt-get install python-pyaudio python3-pyaudio
```

### 📦 Python Environment Setup

Follow these steps to set up your Python environment:

1. Make sure you have `pip-tools` installed:
   
    ```shell
    python -m pip install pip-tools
    ```

2. Compile the dependencies listed in `requirements.in` into `requirements.txt`:

    ```shell
    pip-compile
    ```

3. Install the dependencies:

    ```shell
    pip install -r requirements.txt
    ```

### 🎉 Success!

You are now ready to start working on the project. ✨ Happy coding!

### 📚 Project Structure

Here's a brief overview of the project structure:

```
Super-Assistant-Project/
│
├── src/                      # Source files
│   ├── main.py               # Main entry point
│   └── ...
│
├── tests/                    # Test cases
│   └── ...
│
├── requirements.in           # List of project dependencies
├── requirements.txt          # Compiled dependencies
├── README.md                 # This file
└── ...
```

### 🧪 Running Tests

To run tests, use the following command:

```shell
pytest
```

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🤝 Contributing

Let's say you want to make a feature that recognizes different
people. We'd call that branch something like `recognize-user-by-voice`
and make a branch for it.

1. Fork the project
2. Create your feature branch (`git checkout -b recognize-user-by-voice`)
3. Commit your changes (`git commit -m 'We can now recognize different users by their voice`)
4. Push to the branch (`git push origin recognize-user-by-voice`)
5. Open a Pull Request


#### Todo: 

- [x] Proof of concept
- [ ] Add more features
- [ ] Add tests




