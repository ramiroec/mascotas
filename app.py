from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = f'https://api.thedogapi.com/v1/images/search?limit=10'
    try:
        response = requests.get(url)
        response.raise_for_status()  #Esto lanzará una excepción para códigos de error
        photos = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        photos = []  # En caso de error, devolvemos una lista vacía
    return render_template('index.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
