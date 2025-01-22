import json

def lambda_handler(event, context):
    try:
        # Extract numbers from the event
        number1 = event.get('number1')
        number2 = event.get('number2')
        
        # Validate inputs
        if number1 is None or number2 is None:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'Both number1 and number2 are required'
                })
            }
        
        # Perform addition
        result = number1 + number2
        
        # Return the result
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Addition successful',
                'result': result
            })
        }
    except Exception as e:
        # Handle errors
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred',
                'error': str(e)
            })
        }
