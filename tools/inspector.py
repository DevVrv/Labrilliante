def inspect_level(request, number = 0):
    if request.user.is_authenticated:
        if request.user.level >= number or request.user.is_superuser == 1:
            return True
        else:
            return False
    else:
        return False

def inspect_type(request, type_num):
    responce = False
    if request.user.is_authenticated:
        
        if request.user.user_type == type_num or request.user.is_superuser == 1:
            responce = True
        else:
            responce == False

        return responce
    else:
        return responce