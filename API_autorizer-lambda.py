import jwt
import base64
import hashlib
import hmac
import time

#função que valida o token
def validar_token_autenticacao(token, chave_secreta):
    try:
        decoded_token = jwt.decode(token, chave_secreta, algorithms=['HS256'])
        return True
    except jwt.exceptions.InvalidTokenError:
        return False

def lambda_handler(event, context):
    #receber dados
    token = event['authorizationToken']
    chave_secreta = 'keyeventsec'
    
    #validar token e enviar autorizador
    if validar_token_autenticacao(token, chave_secreta):
        decoded_token = jwt.decode(token, chave_secreta, algorithms=['HS256'])
        id_usuario = decoded_token['dados']['id_usuario']
        
        authResponse = {
            "principalId": id_usuario,
            "policyDocument": {
                "Version": "2023-06-18",
                "Statement": [
                    {
                        "Action": "execute-api:Invoke",
                        "Effect": 'Allow',
                        "Resource": ["arn:aws:execute-api:eu-west-2:*/*/*/*"]
                    }
                ]
            }
        }
    else:
        id_usuario = "unknown"
        authResponse = {
            "principalId": id_usuario,
            "policyDocument": {
                "Version": "2023-06-18",
                "Statement": [
                    {
                        "Action": "execute-api:Invoke",
                        "Effect": 'deny',
                        "Resource": ["arn:aws:execute-api:eu-west-2:*/*/*/*"]
                    }
                ]
            }
        }

    return authResponse
    
#input teste exemplos:
#
#{
#  "authorizationToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYWRvcyI6eyJpZF91c3VhcmlvIjoia2x5bjMifSwiZXhwIjoxNjg2NjIyOTAyLCJwZXJtaXNzaW9ucyI6WyJleGVjdXRlLWFwaTpJbnZva2UiXX0.LbCiF_uo3I4GoFc1s89itGy--dzhpTMgtQY3DDXLsY4"
#}
