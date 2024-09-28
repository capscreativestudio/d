from flask import Flask, render_template, request
import random

# ... (Code du générateur de prompt - identique au précédent)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    # Génération du prompt après soumission du formulaire
    prompt = generer_prompt()
    return render_template('index.html', prompt=prompt)
  else:
    # Affichage initial du formulaire
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
