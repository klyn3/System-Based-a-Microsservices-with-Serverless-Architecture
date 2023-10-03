import json
import json
import boto3

#instanciar base de dados
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('Events')

def lambda_handler(event, context):
    #receber dados
    id_user = event['IdUser']
    id_event =event['iDEvent']
    Event_Name = event.get('Event_Name')
    Event_Data = event.get('Event_Data')
    Event_Description = event.get('Event_Description')
    Event_Local = event.get('Event_Local')
    
    try:
        #modificar valores na base de dados conforme os dados recebidos
        if Event_Name and Event_Data and Event_Description and Event_Local:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Name = :val1, Event_Data = :val2 ,Event_Description = :val3 ,Event_Local = :val4 ',
                ExpressionAttributeValues={
                    ':val1': Event_Name,
                    ':val2': Event_Data,
                    ':val3': Event_Description,
                    ':val4': Event_Local
                    
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Name and Event_Data and Event_Description:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Name = :val1, Event_Data = :val2 ,Event_Description = :val3',
                ExpressionAttributeValues={
                    ':val1': Event_Name,
                    ':val2': Event_Data,
                    ':val3': Event_Description
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Name and Event_Data and Event_Local:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Name = :val1, Event_Data = :val2 ,Event_Local = :val3',
                ExpressionAttributeValues={
                    ':val1': Event_Name,
                    ':val2': Event_Data,
                    ':val3': Event_Local
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Name and Event_Local and Event_Description:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Name = :val1, Event_Local = :val2 ,Event_Description = :val3',
                ExpressionAttributeValues={
                    ':val1': Event_Name,
                    ':val2': Event_Local,
                    ':val3': Event_Description
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Local and Event_Data and Event_Description:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Local = :val1, Event_Data = :val2 ,Event_Description = :val3',
                ExpressionAttributeValues={
                    ':val1': Event_Local,
                    ':val2': Event_Data,
                    ':val3': Event_Description
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Name and Event_Data:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Name = :val1, Event_Data = :val2',
                ExpressionAttributeValues={
                    ':val1': Event_Name,
                    ':val2': Event_Data,
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Name and Event_Local:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Name = :val1, Event_Local = :val2',
                ExpressionAttributeValues={
                    ':val1': Event_Name,
                    ':val2': Event_Local,
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Name and Event_Description:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Name = :val1 ,Event_Description = :val3',
                ExpressionAttributeValues={
                    ':val1': Event_Name,
                    ':val3': Event_Description
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Data and Event_Description:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Data = :val2 ,Event_Description = :val3',
                ExpressionAttributeValues={
                    ':val2': Event_Data,
                    ':val3': Event_Description
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Data and Event_Local:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Data = :val2 ,Event_Local = :val3',
                ExpressionAttributeValues={
                    ':val2': Event_Data,
                    ':val3': Event_Local
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Local and Event_Description:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Local = :val2 ,Event_Description = :val3',
                ExpressionAttributeValues={
                    ':val2': Event_Local,
                    ':val3': Event_Description
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Name:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Name = :val1',
                ExpressionAttributeValues={
                    ':val1': Event_Name
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Data:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Data = :val2',
                ExpressionAttributeValues={
                    ':val2': Event_Data
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Description:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Description = :val3',
                ExpressionAttributeValues={
                    ':val3': Event_Description
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        elif Event_Local:
            response = table.update_item(
                Key={
                    'IdUser': id_user,
                    'iDEvent': id_event
                    },
                UpdateExpression='SET Event_Local = :val4',
                ExpressionAttributeValues={
                    ':val4': Event_Local
                     }
            )
            return {"status_code": 200, "message" :"sucefull"}
        else:
                return None
    except:
        raise
    
#input teste exemplos:
#
#{
#  "IdUser": 45856,
#  "iDEvent": 3,
#  "Event_Local": "Covilha"
#}