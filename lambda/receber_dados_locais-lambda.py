import json
import boto3
from boto3.dynamodb.conditions import Key

# Instanciar base de dados
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('local_events')

def lambda_handler(event, context):
    # Receber dados
    id_user = event['IdUser']
    local_name = event.get('local_name')
    
    try:
        # Procurar dados de um local ou os locais de um utilizador
        if local_name:
            response = table.get_item(
                Key={
                    'IdUser': id_user,
                    'local_name': local_name
                }
            )
            if 'Item' in response:
                return response['Item']
            else:
                return None
        else:
            response = table.scan(
                FilterExpression='IdUser = :id_user',
                ExpressionAttributeValues={
                    ':id_user': id_user
                }
            )
            if 'Items' in response:
                return response['Items']
            else:
                return None
    except:
        raise

#input teste exemplos:
#
#Dados de um local
#
#{
#  "IdUser": 1,
#  "local_name": "lavandariax"
#}
#
#Dados dos locais de um dado utilizador
#
#{
#  "IdUser": 1
#}
