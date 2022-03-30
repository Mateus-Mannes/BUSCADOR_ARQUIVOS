from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'Console'

executables = [
    Executable('organizarArquivos.py', base=base, target_name = 'buscarArquivos')
]

setup(name='buscarArquivos',
      version = '1',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
