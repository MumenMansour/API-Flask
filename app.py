from flask import Flask, jsonify


# create a flask app
app = Flask (__name__) 

#criar uma lista 
lojas = [
    {
        'name': 'magazine',
        'itens':[
            {
                'name': 'Jaqueta',
                'price': 300
        }
        ]
    }
]

# define the route POST 

#cria uma nova loja
#post /loja/ data:{name: }

#app cria rota para o post
@app.route('/loja/', methods=['POST'])
def create_loja():
    #return 'create loja'
    pass


@app.route('/loja')
def get_loja():
    return jsonify ({'lojas': lojas})
    


app.run()