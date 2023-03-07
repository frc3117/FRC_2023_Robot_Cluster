from fastapi.responses import JSONResponse

def response(data=None, status_code=200, message='success', error_code=0, error_message=''):
    return JSONResponse(
        status_code=status_code, 
        content={
            'data': data,
            'message': message,
            'error_code': error_code,
            'error_message': error_message
        })