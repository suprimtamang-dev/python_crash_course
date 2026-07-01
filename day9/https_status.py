def http_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 201:
            return "successfully created"
        case 202:
            return "Accepted"
        case 203:
            return "Not Authorized"
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        
        #   _ is a default case 
        case _:
            return "Something's wrong with the internet"
        
print("http_status(200)=", http_status(200))