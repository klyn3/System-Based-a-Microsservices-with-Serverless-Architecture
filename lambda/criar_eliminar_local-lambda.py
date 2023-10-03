import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

#instanciar base de dados
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('local_events')

def lambda_handler(event, context):
    
    #receber dados
    http_method = event['headers']['httpmethod']
    body = event['body']
    id_user = body['IdUser']
    local_name = body['local_name']
    local_cord = body.get('local_cord')
    local_end = body.get('local_end')
    
    #verificar method
    if http_method == 'POST':
        try:
            #criar item na base de dados
            response=table.put_item(Item={
                'IdUser': id_user,
                'local_name': local_name,
                'local_cord': local_cord,
                'local_end': local_end,
            })
            return {"status_code": 200, "message" :"sucefull add"}
        except:
            raise
    elif http_method == 'DELETE':
        try:
            #eliminar item da base de dadso
            table.delete_item(
                Key={
                    'IdUser': id_user,
                    'local_name': local_name,
                }
            )
            return {"status_code": 200, "message" :"sucefull delete"}
        except:
            raise
    else:
        return {"statusCode": 400, "message": "invalid http method"}
        
#input teste exemplos:
#method Post
#
#{
#  "IdUser": 1,
#  "local_name": "lavandariax",
#  "local_end": "Av. Eugénio de Andrade 19, 6230-296 Fundão",
#  "local_cord": "40.14518710422179,-7.499340224276605"
#}
#
#method Delete
#
#{
#  "IdUser": 1,
#  "local_name": "lavandariax"
#}


