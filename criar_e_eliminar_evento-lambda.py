import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

#instanciar base de dados
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('Events')

def lambda_handler(event, context):
    
    #receber dados
    http_method = event['headers']['httpmethod']
    body = event['body']
    id_user = body['IdUser']
    id_event = body.get('iDEvent')
    Event_Name = body.get('Event_Name')
    Event_Data = body.get('Event_Data')
    Event_Description = body.get('Event_Description')
    Event_Local = body.get('Event_Local')
    
    #verificar method 
    if http_method == 'POST':
        try:
            #receber ultimo idevento da base de dados
            response = table.query(
                KeyConditionExpression=Key('IdUser').eq(id_user),
                ProjectionExpression='iDEvent',
                Limit=1,
                ScanIndexForward=False,
                ConsistentRead=True
            )
            items = response['Items']
            if items:
                iDEvent = items[0]['iDEvent'] + 1
            else:
                iDEvent = 1
                
            #criar item na base de dados
            
            response = table.put_item(Item={
                'IdUser': id_user,
                'iDEvent': iDEvent,
                'Event_Name': Event_Name,
                'Event_Data': Event_Data,
                'Event_Description': Event_Description,
                'Event_Local': Event_Local,
            })
            return {"statusCode": 200, "message": "Successfully added"}
        except Exception as e:
            return {"statusCode": 500, "message": str(e)}
    elif http_method == 'DELETE':
        try:
            #eliminar item da base de dados
            table.delete_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                }
            )
            return {"statusCode": 200, "message": "Successfully deleted"}
        except Exception as e:
            return {"statusCode": 500, "message": str(e)}
    else:
        return {"statusCode": 400, "message": "Invalid http method"}
        

#input teste exemplos:
#method Post
#{
#  "IdUser": 45856,
#  "Event_Data": 202305282000,
#  "Event_Description": "levar agua",
#  "Event_Name": "caminhada"
#  "Local_Name": "Covilhã"
#}
#
#method Delete
#{
#  "IdUser": 45856,
#  "iDEvent": 4
#}


