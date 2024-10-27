from flask import Flask, render_template, request
import tiktoken

app = Flask(__name__)

# cargamos el modelo de tokenización
encoding = tiktoken.get_encoding('gpt2')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # obtener la oración ingresada por usuario
        text = request.form['input_text']
        
        # tokenizamos el texto
        tokens = encoding.encode(text)
        
        # decodificamos los tokens
        decode_text = encoding.decode(tokens)
        
        # geramos la lista de tokens con sus correspondientes palabras, subpalabras o caracteres
        token_text_pairs = [(token, encoding.decode([token])) for token in tokens]
        
        # enviamos los datos a la web para que lo vea el usuario
        return render_template('index.html', text = text, tokens = tokens, decode_text = decode_text, token_text_pairs = token_text_pairs)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
