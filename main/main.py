import marshal
import os.path
import py_compile
import subprocess
import sys
import timeit
import time
import dis
from tempfile import NamedTemporaryFile
from terminaltables import AsciiTable

print(''' --------------USAGE main.py-----------------------
To see how to run the tasks USE:
$ python3 main.py task# (# = 1,2,3,4,5)
''')

def table_task1(dict):
    if True:
        all_functions = sorted(dict.items(), key=lambda item: item[1])
        print('PROGRAM   |    RANK    | TIME ELAPSED')
        count = 1
        for i in all_functions:
            print(i[0], '\t',count, '\t', i[1], 'seconds')
            count += 1


def task1():
    print('''
    ------------TASK1 USAGE----------------
    command:  $ python3 main.py task1 [files]

    This program prints and compares time 
    execution of all files which are located 
    inside of current directory.
    -----------OUTPUT---------------''')

    dict = {}
    for i in sys.argv[2:]:
        time_start = time.time()
        process = subprocess.run(['python3', i], stdout=subprocess.PIPE)

        dict.update({i : time.time() - time_start})
    table_task1(dict)

def task2():
    print('''-----------TASK2 USAGE----------------
    command:  $ python3 main.py task2 -py [files]
    
    This program prints byte-code
    of files which are located 
    inside of current directory.
    -----------OUTPUT---------------''')
    if sys.argv[2] == '-py':
        for i in sys.argv[3:]:
            print(f'------------{i.upper()}------------')
            py_compile.compile(i)
            with open(i, 'r') as file:
                code = file.read()
            byte_code = dis.Bytecode(code)
            for line in byte_code:
                print(f'{line.opname}\t{line.argval}')


def task3():
    print('----PATH TO PYC FILES-------')
    for file in os.listdir('__pycache__/'):
        print(f'__pycache__/{file}')
    print('''-----------TASK3 USAGE----------------
    $ python3 main.py task3 -pyc [path to pyc files]
    $ python3 main.py task3 -s "python code (string)"

    This program prints byte-code
    of .pyc files which are located 
    inside of __pycache__ directory.
    -----------OUTPUT---------------''')

    if sys.argv[2] == '-pyc':
        for i in sys.argv[3:]:
            print(f'--------------{i}--------------')
            with open(i, 'rb') as pyc_file:
                pyc_file.seek(16)
                byte_code = marshal.load(pyc_file)
                for h in dis.get_instructions(byte_code):
                    print(f'{h.opname}\t{h.argval}')
    elif sys.argv[2] == '-s':
        print('------------------------------')
        for i in sys.argv[3:]:
            c = compile(f'{i}', '<string>', 'exec')
            byte_code = dis.Bytecode(c)
            for j in byte_code:
                print(f'{j.opname}\t{j.argval}')


def print_task_4_5():
    if sys.argv[3] == '-pyc':
        for i in sys.argv[4:]:
            print(f'--------------{i}--------------')
            with open(i, 'rb') as pyc_file:
                pyc_file.seek(16)
                byte_code = marshal.load(pyc_file)
                for h in dis.get_instructions(byte_code):
                    print(f'{h.opname}\t{h.argval}')
    elif sys.argv[3] == '-s':
        for i in sys.argv[4:]:
            c = compile(f'{i}', '<string>', 'exec')
            byte_code = dis.Bytecode(c)
            for j in byte_code:
                print(f'{j.opname}\t{j.argval}')
    elif sys.argv[3] == '-py':
        for i in sys.argv[4:]:
            print(f'------------{i.upper()}------------')
            py_compile.compile(i)
            with open(i, 'r') as file:
                code = file.read()
            byte_code = dis.Bytecode(code)
            for line in byte_code:
                print(f'{line.opname}\t{line.argval}')
def compile_task_4_5():
    if sys.argv[3] == '-py':
        for i in sys.argv[4:]:
            py_compile.compile(i, cfile=f'{i}c')
        print(os.listdir())
    if sys.argv[3] == '-s':
        for i in sys.argv[4:]:
            with NamedTemporaryFile('w', delete=True) as f:
                f.write(i)
                f.seek(0)
                py_compile.compile(f.name, cfile="out.pyc")
        print(os.listdir())

def task4():
    print('''
    -----------TASK4 USAGE----------------
    FOR COMPILE USE:
        command:  $ python3 main.py task4 compile -py [files]
        command:  $ python3 main.py task4 compile -s "python code (string)"
    FOR PRINTING BYTECODE USE:
        command:  $ python3 main.py task4 print -py [files]
        command:  $ python3 main.py task4 print -pyc [pyc files]
        command:  $ python3 main.py task4 print -s "python code (string)"
        
    This program prints byte-code of python files and text which are located 
    in current directory If user wants to get bytecode  of .py file, the .pyc 
    file will be created with the same name. If user wants to get bytecode of 
    text, program stores this text bytecode to 'out.pyc' file and prints.
    -------------------------------OUTPUT--------------------------------------''')
    if sys.argv[2] == 'compile':
        compile_task_4_5()
    elif sys.argv[2] == 'print':
        print_task_4_5()


def table_task5(dict):
        dict = {'src1.py': {'LOAD_CONST': 5, 'IMPORT_NAME': 1, 'STORE_NAME': 2, 'MAKE_FUNCTION': 1, 'RETURN_VALUE': 1},
                'src2.py': {'LOAD_CONST': 3, 'MAKE_FUNCTION': 1, 'STORE_NAME': 1, 'RETURN_VALUE': 1},
                'src3.py': {'LOAD_CONST': 3, 'MAKE_FUNCTION': 1, 'STORE_NAME': 1, 'RETURN_VALUE': 1},
                'src4.py': {'LOAD_CONST': 3, 'MAKE_FUNCTION': 1, 'STORE_NAME': 1, 'RETURN_VALUE': 1}}

        instructions = ['LOAD_CONST', 'IMPORT_NAME', 'STORE_NAME', 'MAKE_FUNCTION', 'RETURN_VALUE', 'LOAD_CONST',
                        'BINARY_OR',
                        'INPLACE_POWER', 'INPLACE_ADD', 'INPLACE_LSHIFT', 'YIELD_FROM', 'SETUP_ANNOTATIONS']

        header = ['INSTRUCTION'] + [key_val for key_val in dict.keys()];
        table_data = [
            header
        ]

        for instruction in instructions:
            row = [instruction]
            for column in dict.keys():
                srcData = dict[column]

                if (instruction in srcData):
                    row.append(dict[column][instruction])
                else:
                    row.append('0')
            table_data.append(row)

        table = AsciiTable(table_data)
        print(table.table)
        f = open("result.txt","w+")
        f.write(table.table)








def compare_task5():
    dict = {'src1.py' : {},
            'src2.py' : {},
            'src3.py' : {},
            'src4.py' : {}}
    if sys.argv[3] == '-py':
        for i in sys.argv[4:]:
            py_compile.compile(i)
            with open(i, 'r') as file:
                code = file.read()
            byte_code = dis.Bytecode(code)
            for line in byte_code:
                if line.opname in dict[f'{i}']:
                    dict[f'{i}'][line.opname] += 1
                else:
                    dict[f'{i}'][line.opname] = 1
    # print(dict.items())
    table_task5({})


def task5():
    print('''
        -----------TASK4 USAGE----------------
        TO COMPARE USE:
            command:  $ python3 main.py task5 compare -py [files]
        

        This program prints table of the # of opnames of py file
        -------------------------------OUTPUT--------------------------------------''')
    if sys.argv[2] == 'compile':
        compile_task_4_5()
    elif sys.argv[2] == 'print':
        print_task_4_5()
    elif sys.argv[2] == 'compare':
        compare_task5()







if __name__ == '__main__':


    if sys.argv[1] == 'task1':
        try:
            task1()
        except IndexError:
            print("Please READ the USAGE")
    elif sys.argv[1] == 'task2':
        try:
            task2()
        except IndexError:
            print("Please READ the USAGE")
    elif sys.argv[1] == 'task3':
        try:
            task3()
        except IndexError:
            print("Please READ the USAGE")
    elif sys.argv[1] == 'task4':
        try:
            task4()
        except IndexError:
            print("Please READ the USAGE")
    elif sys.argv[1] == 'task5':
        try:
            task5()
        except IndexError:
            print("Please READ the USAGE")






