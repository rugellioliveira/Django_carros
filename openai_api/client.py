from openai import OpenAI

client = OpenAI(api_key = 'insira aqui sua chave')

def get_car_ai_bio(model, brand, year):
    message = '''
            Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres.
            Fale coisas específicas do modelo e especificações técnicas.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages = [
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens = 1000,
        model = 'gpt-3.5-turbo'
    )
    return response.choise[0].message.content