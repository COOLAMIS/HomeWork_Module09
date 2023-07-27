users_contact = {}
list_end = ['good bye', 'close', 'exit']

def decorator_input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError:
            return('Give me correct data please')
        except IndexError:
            return('Give me correct data please')
        except KeyError:
            return('Give me correct data please')
    return wrapper

@decorator_input_error
def hello(*args):
    return 'How can I help you?'

@decorator_input_error
def add(*args):
    name = args[0]
    phone = args[1]
    users_contact[name] = phone
    return 'Add success'

@decorator_input_error
def change_number(*args):
    name = args[0]
    phone = args[1]
    users_contact[name] = phone
    return 'Change success'

@decorator_input_error
def phone(*args):
    name_user = args[0]
    phone = args[1]  
    for name, phone in users_contact.items():
        if name_user == name:
            return phone
        
@decorator_input_error
def show_all(*args):
    return users_contact

@decorator_input_error
def no_command(*args):
    return 'unknown_command'

dict_command = {'hello': hello,
                'add': add,
                'change': change_number,
                'phone': phone,
                'show': show_all,
                }

def parser(text: str) -> tuple[callable, tuple[str]]:
    text1 = text.split()
    if text1[0] in dict_command.keys():
        return dict_command.get(text1[0]), text.replace(text1[0], '').strip().split()
    return no_command, text

def main():
    while True:
        user_input = input('>>>')
        user_input = user_input.lower()
        
        if user_input in list_end:
            print('Good bye!')
            break
        
        command, data = parser(user_input)
        result = command(*data)
        print(result)
        
        
        
        
if __name__ == '__main__':
    main()