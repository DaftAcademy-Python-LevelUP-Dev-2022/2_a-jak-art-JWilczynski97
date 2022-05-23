from functools import wraps


def greeter(func):
    def inner_func(*args):
        return "Aloha " + ' '.join([word.lower().capitalize() for word in func(*args).split(" ")])
    return inner_func


def sums_of_str_elements_are_equal(func):
    def inner(*args):
        num1, num2 = func(*args).split(" ")
        digitals_1 = list(num1) if '-' not in num1 else [num1[:2]] + ['-'+dig for dig in list(num1)[2:]]
        digitals_2 = list(num2) if '-' not in num2 else [num2[:2]] + ['-'+dig for dig in list(num2)[2:]]
        sum1 = sum([int(i) for i in digitals_1])
        sum2 = sum([int(i) for i in digitals_2])
        mark = ' == ' if sum1 == sum2 else ' != '
        return str(sum1) + mark + str(sum2)
    return inner


def format_output(*new_keys):
    def inner(func_to_decor):
        def inner2(*args, **kwargs):
            orig_dict = func_to_decor(*args, **kwargs)
            keys_to_stay = list()
            for a in new_keys:
                for check in a.split('__'):
                    if check not in orig_dict:
                        raise ValueError()
                if a in orig_dict:
                    keys_to_stay.append(a)
                elif '__' in a:
                    keys_to_stay.append(a)
                    orig_dict[a] = ' '.join([orig_dict[k] for k in a.split('__')])
                # elif a not in orig_dict:
                #     raise ValueError()
            tmp = {key: orig_dict[key] for key in keys_to_stay}
            for k, v in tmp.items():
                if v == '':
                    tmp[k] = 'Empty value'
            return tmp
        return inner2
    return inner


def add_method_to_instance(klass):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, wrapper)
        return wrapper
    return decorator
