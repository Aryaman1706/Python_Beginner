def cough_dec(function):
    
    def function_wrapper():
        #code before function
        print('*cough*')
        function()
        #code after function
        print('*cough*')

    return function_wrapper


@cough_dec
def question():
    print('can you give me a discount on that?')

@cough_dec
def answer():
    print("its only 50p you cheapskate")

question()
answer()