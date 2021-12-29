
from flask import Flask, render_template
app = Flask(__name__)

# Criar a 1 pagina do site
# route -> rota do site /contatos, /produtos
# função -> que indica onde a rota+template estão
# template -> templates das rotas
@app.route("/")

def homepage():
    return render_template('homepage.html')

@app.route('/contatos')

def contatos():
    return render_template('contatos.html')


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

