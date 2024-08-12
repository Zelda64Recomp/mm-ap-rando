#include <stdio.h>
#include <librecomp/recomp.h>
#include <Python.h>

void generate() {
  Py_Initialize();
  PyRun_SimpleString("print('Hello from Python!')");
  Py_Finalize();
}

extern "C" void recomp_main(uint8_t* rdram, recomp_context* ctx) {
  generate();
}
