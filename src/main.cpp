#include "utils.h"

#include <stdio.h>
#include <dlfcn.h>
#include <Python.h>
#include <librecomp/recomp.h>

void generate() {
  auto dylib_path = get_mod_dylib_path();

  // initialize python
  Py_SetProgramName(L"Generate.py");
  Py_Initialize();
  PyRun_SimpleString("import sys");
  PyRun_SimpleString("print('Hello from Python!')");
  
  // remove last path entry and add the zip file's dep folder based on the current dynamic library path
  PyRun_SimpleString("sys.path.pop()");
  auto mod_zip_path = std::string("sys.path.insert(0, '") + get_mod_zip_path() + "/deps/')";
  PyRun_SimpleString(mod_zip_path.c_str());

  // print the python path
  PyRun_SimpleString("print(sys.path)");

  // test the import
  PyRun_SimpleString("import requests");
  PyRun_SimpleString("print(requests.__file__)");
  
  // finalize python
  Py_Finalize();
}

extern "C" void recomp_main(uint8_t* rdram, recomp_context* ctx) {
  generate();
}
