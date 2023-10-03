import hashlib
import secrets
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

#instanciar base de dados
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('User_Events')

def lambda_handler(event, context):
    #receber dados
    username = event['username']
    email = event['email']
    password = event['password']
    
    #gerar um salt
    salt = secrets.token_hex(16)
    #encriptar password
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

    try:
        #verificar existencia de utilizador
        response = table.scan(
            FilterExpression=Attr('email').eq(email) | Attr('user_name').eq(username),
            ProjectionExpression='IdUser'
        )
        items = response['Items']
        if items:
            return {"status_code": 400, "message": "Client already exists"}
            
        # receber ultimo idUser da base de dados
        response = table.scan(
            ProjectionExpression='IdUser'
        )
        items = response['Items']
        if items:
            max_id = max([int(item['IdUser']) for item in items])
            new_user_id = max_id + 1
        else:
            new_user_id = 1
            
        #criar item na base de dados
        response = table.put_item(Item={
            'user_name': username,
            'IdUser': new_user_id,
            'email': email,
            'password': hashed_password,
            'salt': salt,
        })
        return {"status_code": 200, "message": "Successfully added"}
    except:
        raise
    
#input teste exemplos:
#
#{
#  "username": "user",
#  "email": "val.0@gmail.com",
#  "password": "value1"
#}