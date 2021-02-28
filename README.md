# Keithfem contributors page
A contributors page generator for [www.keithfem.com](https://www.keithfem.com/).

## Usage

```bash
$ poetry install
$ poetry run ./src/main.py > contributors.html
```

## W3C Validator

```bash
$ curl -H "Content-Type: text/html; charset=utf-8" --data-binary @contributors.html https://validator.w3.org/nu/?out=gnu
```

<sub><sup>Keith F'em, a community radio experiment, is presented by Keith in conjuction with SP2. hello@keithfem.com</sup></sub>
