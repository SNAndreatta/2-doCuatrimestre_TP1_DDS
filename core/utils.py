redes = [
    ("instagram", ["instagram"]),
    ("twitter", ["twitter", "x.com"]),
    ("facebook", ["facebook"]),
    ("flickr", ["flickr"]),
    ("linkedin", ["linkedin"]),
    ("youtube", ["youtube"]),
    ("tiktok", ["tiktok"]),
]

def obtener_red_social(link: str) -> str:
    """
    Detecta el nombre de la red social a partir de un link.
    Si no la encuentra devuelve 'desconocido'.
    """
    link = link.lower()
    for nombre, alias_list in redes:
        for alias in alias_list:
            if alias in link:
                return nombre
    return "desconocido"

def limpiar_links(raw: str) -> list[str]:
    """
    Divide una cadena de links separados por '//' y devuelve solo los válidos.
    Se descartan vacíos o fragmentos incompletos (ej: 'https:', 'http:').
    """
    links = []
    for parte in raw.split("//"):
        parte = parte.strip()
        if not parte:
            continue
        # reconstruimos si falta esquema
        if parte.startswith("http"):
            link = parte
        else:
            link = "https://" + parte
        # filtramos falsos positivos tipo "https:" o "http:"
        if link.lower() in ("https:", "http:"):
            continue
        links.append(link)
    return links