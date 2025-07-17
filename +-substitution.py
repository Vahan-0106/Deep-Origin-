import dis
import marshal
import types

with open("__pycache__/Addition.cpython-313.pyc", "rb") as f:
    f.read(16)
    code = marshal.load(f)

code_bytes = bytearray(code.co_code)

for i in range(len(code_bytes)):
    if code_bytes[i] == 23:
        code_bytes[i] = 24

new_code = types.CodeType(
    code.co_argcount,
    code.co_posonlyargcount,
    code.co_kwonlyargcount,
    code.co_nlocals,
    code.co_stacksize,
    code.co_flags,
    bytes(code_bytes),  
    code.co_consts,
    code.co_names,
    code.co_varnames,
    code.co_filename,
    code.co_name,
    code.co_qualname,       
    code.co_firstlineno,
    code.co_linetable,      
    code.co_exceptiontable,  
    code.co_freevars,
    code.co_cellvars
)


exec(new_code)
