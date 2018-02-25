
__all__ = [
    'login',
    'register'
]


def login ( username, password):
    """
    IMPLEMENTATION LOGIC - FETCH FROM DB 
    THE HASH AND USERNAME TO VALIDATE THE
    WORKING
    """
    result = 'True'
    print "The function is working:login"
    print "The username is"
    print username
    print "The password is"
    print password
    return bool(result)

def register (username, email, phone):

    """
    IMPLEMENTATION LOGIC - INSERT INTO DB
    RELEVANT VALUES

    """
    print "The function is working:register"

