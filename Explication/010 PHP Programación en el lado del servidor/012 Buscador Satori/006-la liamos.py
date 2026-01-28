import requests
from lxml import html
import mysql.connector
import time
from urllib.parse import urljoin, urlparse

URLS = ["https://elpais.com"]

DB_HOST = "localhost"
DB_USER = "satori"
DB_PASSWORD = "Satori123$"
DB_NAME = "satori"

visitadas = set()

def busca(urls, profundidad=0, max_profundidad=1):
    if profundidad > max_profundidad:
        return

    for url in urls:
        if url in visitadas:
            continue

        visitadas.add(url)
        time.sleep(5)

        try:
            print(f"Visitando: {url}")

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
                }
            )
            response.raise_for_status()

            tree = html.fromstring(response.content)

            title = tree.xpath("//title/text()")
            web_title = title[0].strip() if title else None
            html_content = response.text[:255]

            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                charset="utf8mb4"
            )

            cur = conn.cursor()
            sql = """
                INSERT INTO paginas (titulo, url, contenido)
                VALUES (%s, %s, %s)
            """
            cur.execute(sql, (web_title, url, html_content))
            conn.commit()

            cur.close()
            conn.close()

            print(f"✔ Guardado: {web_title}")

            enlaces = tree.xpath("//a/@href")
            enlaces_validos = []

            for enlace in enlaces:
                enlace = urljoin(url, enlace)
                if urlparse(enlace).scheme in ("http", "https"):
                    enlaces_validos.append(enlace)

            busca(enlaces_validos, profundidad + 1)

        except Exception as e:
            print(f"✖ Error en {url}: {e}")

busca(URLS)
