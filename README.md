Widow Sweeper
===================


The aim of this project is to provide a simple CLI using python 3 in order to evaluate HTTP security headers defined by OWASP [Security Headers](https://www.owasp.org/index.php/Security_Headers).

----------

Requirements and installation
-------------

In order to run this program you will need and installation of **python 3** and **pip 3** for dependency installation.

> **Note:**

> - The latest version of python 3 is recommended for a better efficiency, currently python 3.6.

After installing python and pip just run the following command to install pip dependencies:

```bash
pip3 install -r requirements.txt
```

Usage
-------------

To display available running options run:

```bash
python3 widow-sweeper.py -h
```
```bash
usage: widow-sweeper.py [-h] [-v] [-c CONFIG] [-u URL] [-m METHOD]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program version and exit
  -c CONFIG, --config CONFIG
                        configuration file in JSON format
  -u URL, --url URL     complete url
  -m METHOD, --method METHOD
                        HTTP method
```

There are two running modes:  **Run a single request** and **Run from configuration file**.

In order to run a single request just define the URL with -u and the HTTP method with -m, take the following as an example:

```bash
python3 widow-sweeper.py -u http://pokeapi.co/api/v2/pokemon/1/ -m GET
```

```bash
=> Security Request 
	- Url: http://pokeapi.co/api/v2/pokemon/1/
	- Method: GET
        - Security headers status:
            :: X-Frame-Options: Safe header
            :: X-XSS-Protection: Safe header
            :: X-Content-Type-Options: Header is missing
            :: Content-Type: Invalid header, should be: text/html;charset=utf-8
```
If you prefer to use a configuration file for multiple requests you can provide a JSON file with -c with the following format:
```javascript
[
  {
    "url": "http://pokeapi.co/api/v2/pokemon/1/",
    "method": "GET"
  },
  {
    "url": "http://pokeapi.co/api/v2/pokemon/2/",
    "method": "GET"
  },
  {
    "url": "http://pokeapi.co/api/v2/pokemon/3/",
    "method": "GET"
  }
]
```
Just run the following command:
```bash
python3 widow-sweeper.py -c example.json
```
```bash
=> Security Request 
	- Url: http://pokeapi.co/api/v2/pokemon/1/
	- Method: GET
        - Security headers status:
            :: X-Frame-Options: Safe header
            :: X-XSS-Protection: Safe header
            :: X-Content-Type-Options: Header is missing
            :: Content-Type: Invalid header, should be: text/html;charset=utf-8
=> Security Request 
	- Url: http://pokeapi.co/api/v2/pokemon/2/
	- Method: GET
        - Security headers status:
            :: X-Frame-Options: Safe header
            :: X-XSS-Protection: Safe header
            :: X-Content-Type-Options: Header is missing
            :: Content-Type: Invalid header, should be: text/html;charset=utf-8
=> Security Request 
	- Url: http://pokeapi.co/api/v2/pokemon/3/
	- Method: GET
        - Security headers status:
            :: X-Frame-Options: Safe header
            :: X-XSS-Protection: Safe header
            :: X-Content-Type-Options: Header is missing
            :: Content-Type: Invalid header, should be: text/html;charset=utf-8
```