import json
import boto3
import os

users_table = os.environ['MOVIES_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

def getMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    movie_id = array_path[-1]
    
    response = table.get_item(
        Key={
            'pk': movie_id,
            'sk': 'info'
        }
    )
    item = response['Item']

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    movie_id = array_path[-1]
    
    body = event["body"]
    body_object = json.loads(body)
    
    table.put_item(
       Item={
            'pk': movie_id,
            'sk': 'info',
            'actors': body_object['actors'],
            'year': body_object['year'],
            'title': body_object['title']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully inserted movie')
    }

def roomsPerDay(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    movie_id = array_path[-1]
    
    body = event["body"]
    body_object = json.loads(body)
    
    response = table.get_item(
        Key={
            'pk': movie_id,
            'sk': body_object["date"]
        }
    )
    
    item = response['Item']

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def getRoom(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    room_id = array_path[-1]
    
    response = table.get_item(
        Key={
            'pk': room_id,
            'sk': 'info'
        }
    )
    
    item = response['Item']

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def getPersonMoviesWatched(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    person_id = array_path[-1]
    
    response = table.get_item(
        Key={
            'pk': person_id
        }
    )
    
    item = response['Item']

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def getPeopleAssist(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    movie_id = array_path[1]
    room_id = array_path[-1]
    
    body = event["body"]
    body_object = json.loads(body)
    
    response = table.get_item(
        Key={
            'pk': '' + movie_id + '-' + room_id
        }
    )
    
    item = response['Item']

    return {
        'statusCode': 200,
        'body': json.dumps('Getting movie')
    }
    
def putPersonsToMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    person_id = array_path[-1]
    
    body = event["body"]
    body_object = json.loads(body)
    
    table.put_item(
       Item={
            'pk': movie_id,
            'sk': 'info',
            'actors': body_object['actors'],
            'year': body_object['year'],
            'title': body_object['title']
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully inserted movie')
    }