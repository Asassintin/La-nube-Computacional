from flask import Flask 
app = Flask(__name__) 

@app.route("/") 
def home(): 
    return """ 
    <!DOCTYPE html> 
    <html> 
    <head> 
        <title>Tenis App</title> 
        <style>
            body { 
                font-family: Arial, sans-serif; 
                text-align: center; 
                margin: 50px; 
                background-color: #f0f8ff;
            }
            h1 { color: #333; }
            .container { 
                max-width: 600px; 
                margin: 0 auto; 
                padding: 20px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
        </style>
    </head> 
    <body>
        <div class="container">
            <h1>🎾 Bienvenido a Tenis App</h1>
            <p>¡Tu aplicación Python está funcionando correctamente en Azure!</p>
            <p>Desplegado con Azure App Service (PaaS)</p>
        </div>
    </body>
    </html> 
    """ 

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5500, debug=True) 