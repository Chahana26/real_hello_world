import os
from cffi import FFI

desired_compiler = 'gcc'
real2_library_path = '/home/chahana/libreal2.a'

absolute_library_path = os.path.abspath(real2_library_path)

####################
# Setup part
####################

if not os.environ.get('CC'):
    os.environ['CC'] = desired_compiler


####################
# Compilation part
####################

ffibuilder = FFI()
# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("void my_new_wrappers(double x,double y);", override=True)


# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("my_real_hello2",''' #include "real_hello_world.h" ''',
                      library_dirs=[os.getcwd()],
                      include_dirs=[os.getcwd()+'/home/chahana'],
                      extra_link_args=[os.path.abspath(real2_library_path), '-lgfortran',])
ffibuilder.compile(verbose=True)
