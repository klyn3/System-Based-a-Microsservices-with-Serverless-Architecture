import json
import boto3
from boto3.dynamodb.conditions import Key

#instanciar base de dados
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('Events')

def lambda_handler(event, context):
    #receber dados
    id_user = event['IdUser']
    id_event =event.get('iDEvent')
    try:
        #receber dados de um evento ou dos eventos de um dado utilizador
        if id_event:
            response = table.get_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                }
                )
            if 'Item' in response:
                return response['Item']
                print(response['Item'])
            else:
                return None
        else:
            response = table.query(
                KeyConditionExpression=Key('IdUser').eq(id_user)
            )
            if 'Items' in response:
                print(response['Items'])
                return response['Items']
            else:
                return None
    except:
        raise
    
#input teste exemplos:
#
#receber deados de um evento
#
#{
#  "IdUser": 45856,
#  "iDEvent": 4
#}
#
#receber dados de um dado utilizador
#
#{
#  "IdUser": 45856
#}