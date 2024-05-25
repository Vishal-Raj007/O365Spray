# O365 SprayMaster - O365 Password Spray Atack Tool

[![Designer-2.jpg](https://i.postimg.cc/dt97gtwg/Designer-2.jpg)](https://postimg.cc/7ffY24CN)

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
  - [Help Options](#help-options)
  - [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Welcome to the O365 SprayMaster! This project is designed to perform password spray attacks on O365 accounts. The script is writen in python3 and uses various thresholds to manage the rate of attempts and includes logging to track progress and results.

## Usage

### Help option

To run the script, use the following command-line options:

```bash
python3 main.py [-h] -u username_list -p passwords_list [-t {slow,medium,fast,veryfast}] [-o output_filename]

options:
  -h, --help    show this help message and exit
  -u, --userList username_list  File name which contain User List.
  -p, --passList passwords_list  File name which contain List of Passwords.
  -t, --threshold {slow,medium,fast,veryfast}   Set the speed threshold for the attack (slow, medium, fast, veryfast). Default is fast.
  -o, --output output_filename  File name which contain User List.
```

### Deployment

1. Clone the repository:

```bash
git clone https://github.com/Vishal-Raj007/O365Spray.git
cd O365Spray
```

2. Install dependencies:

```
pip3 install -r requirements.txt
```

3. Run the script:

```bash
chmod +x main.py
python3 main.py -u username_list -p passwords_list -t {slow,medium,fast,veryfast} -o output_filename
```

## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, feel free to reach out:

    Author: Vishal Raj
    Email: vishalraj.infosecpro@gmail.com
