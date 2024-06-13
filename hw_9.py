import sys


def log_numbers(name, log_level=None):
    #lagu = ['INFO', 'ERROR', 'WARNING', 'DEBUG', ]
    info_counter = 0
    debug_counter = 0
    warning_counter = 0
    error_counter = 0
    with open(name, mode='r', encoding='utf=8') as file:
        if not log_level:
            for line in file:
                if 'INFO' in line:
                    info_counter += 1
                elif 'DEBUG' in line:
                    debug_counter += 1
                elif 'WARNING ' in line:
                    warning_counter += 1
                elif 'ERROR' in line:
                    error_counter += 1
            result = f'info : {info_counter} , debug : {debug_counter}, warning : {warning_counter}, error : {error_counter}'
        else:
            counter = 0
            for line in file:
                if log_level.upper() in line.upper():
                    counter += 1
            result = f"{log_level} : {counter}"
        return result












if __name__ == "__main__":
    print(log_numbers(sys.argv[1], sys.argv[2]))
