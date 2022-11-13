import os
import requests


def get_lines(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    data = response.text
    lines = data.split("\n")
    lines = [line.rstrip() for line in lines]
    return lines


urls = {
    "pj_contains": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRr7ArDmTqBjZiDXksNv76d9KTz_dEOSJSSPQwVGFYgiTZOSK2qEsplJMm-Ggwa5QbYsj-ZaNHn1ymg/pub?gid=1466763224&single=true&output=csv",
    "pj_ends_with": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRr7ArDmTqBjZiDXksNv76d9KTz_dEOSJSSPQwVGFYgiTZOSK2qEsplJMm-Ggwa5QbYsj-ZaNHn1ymg/pub?gid=824889827&single=true&output=csv",
    "pj_has_word": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRr7ArDmTqBjZiDXksNv76d9KTz_dEOSJSSPQwVGFYgiTZOSK2qEsplJMm-Ggwa5QbYsj-ZaNHn1ymg/pub?gid=324213418&single=true&output=csv",
    "aer_contains": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRr7ArDmTqBjZiDXksNv76d9KTz_dEOSJSSPQwVGFYgiTZOSK2qEsplJMm-Ggwa5QbYsj-ZaNHn1ymg/pub?gid=0&single=true&output=csv",
    "aer_ends_with": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRr7ArDmTqBjZiDXksNv76d9KTz_dEOSJSSPQwVGFYgiTZOSK2qEsplJMm-Ggwa5QbYsj-ZaNHn1ymg/pub?gid=721484720&single=true&output=csv",
    "list_strings": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRr7ArDmTqBjZiDXksNv76d9KTz_dEOSJSSPQwVGFYgiTZOSK2qEsplJMm-Ggwa5QbYsj-ZaNHn1ymg/pub?gid=1185843739&single=true&output=csv",
}


def get_info():
    info = {}
    for key in urls:
        lines = get_lines(urls[key])
        info[key] = lines
    return info
