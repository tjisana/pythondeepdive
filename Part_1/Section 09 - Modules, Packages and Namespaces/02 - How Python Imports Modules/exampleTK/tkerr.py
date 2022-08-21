from types import ModuleType
import os
import sys

module_name = 'word'
module_file_name = 'word.py'

dir_path = os.path.dirname(os.path.realpath(__file__))
module_path = os.path.join(dir_path, module_file_name)

with open(module_path, 'r') as code_file:
    source = code_file.read()


mod = ModuleType(module_name)
mod.__file__ = module_path


sys.modules[module_name] = mod

code = compile(source, module_path, mode='exec')
exec(code, mod.__dict__)
