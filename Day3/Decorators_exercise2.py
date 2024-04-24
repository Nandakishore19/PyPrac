import random
def retry(func):
    max_attempts = 7
    curr_attempt = 1
    def wrapper():
        nonlocal curr_attempt
        while curr_attempt<=max_attempts:
            result = func()
            if result:
                print("Success!! at attempt number {}".format(curr_attempt))
                break
            print("Retry- Current Attempt number {}".format(curr_attempt))
            curr_attempt+=1
        else:
            print("Max attempts reached...")
        return result
    return wrapper
        
            

    
@retry
def random_number():
    k = random.randint(1,11)
    if k<3:
        return True
    else:
        return False

random_number()