# Resume

Parameter used to add a new item to the list in your profile file.

## Usage

```bash
linuxp add --help

=============== Output ===============

usage: linuxp add [-h] -m {package,alias,script,file}

optional arguments:
-h, --help            show this help message and exit

Usage: linuxp add [OPTIONS]:
-m {package,alias,script,file}, --module {package,alias,script,file}

=============== Output ===============
```

## Flow

<center>

``` mermaid
graph TD
    L[linuxp] -->|type command| a(add)
    a ---> option_a{arguments}
    option_a --->|add| arg_a_module[module]
```

</center>