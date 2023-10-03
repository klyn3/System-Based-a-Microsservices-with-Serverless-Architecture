import json
import hashlib
import time
import jwt
import boto3
from boto3.dynamodb.conditions import Key

#instanciar base de dados
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('User_Events')

#função que cria o token
def criar_token(chave_secreta, dados_payload):
    #criar payload com os dados recebidos
    payload = {
        'dados': dados_payload,
        'exp': int(time.time()) + 3600,
        'permissions': ['execute-api:Invoke']
    }
    #codificar token
    token = jwt.encode(payload, chave_secreta, algorithm='HS256')
    return token

def lambda_handler(event, context):
    #receber dados
    user_name = event['username']
    password = event['password']
    
    #defenir chave secreta
    chave_secreta = 'keyeventsec'
    dados_payload = {'id_usuario': user_name}

    try:
        #procurar dados na base de dados
        response = table.query(
            KeyConditionExpression='user_name = :id',
            ExpressionAttributeValues={
                ':id': user_name,
            },
            ProjectionExpression='password, salt, IdUser'
        )
        #receber dados da base de dados
        if response['Items']:
            item = response['Items'][0]
            passwordhash = item['password']
            salt = item['salt']
            IdUser = item['IdUser']
            
            #encriptar password recebida pelo utilizador
            encrypted_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
            
            #verificar password
            if encrypted_password == passwordhash:
                token = criar_token(chave_secreta, dados_payload)

                return {"status_code": 200, "message": "true", "token": token}
            else:
                return {"status_code": 200, "message": "False"}
        else:
            return {"status_code": 200, "message": "no user"}
    except:
        raise
    
    
#input teste exemplos:
#
#{
#  "username": "user",
#  "password": "value1"
#}
