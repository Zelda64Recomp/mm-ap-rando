#include "utils.h"

#include <stdio.h>
#include <dlfcn.h>
#include <Python.h>
#include <librecomp/recomp.h>
#include <filesystem>

void generate() {
  auto dylib_path = get_mod_dylib_path();

  // initialize python
  // Py_SetProgramName(L"Generate.py");
  
  PyConfig config;
  PyConfig_InitPythonConfig(&config);
  config.isolated = 1;

  std::filesystem::path player_files_path = get_mod_folder() / "Players";
  const char *argv[] = {
    "Generate.py",
    "--player_files_path",
    player_files_path.c_str()
  };

  PyStatus status = PyConfig_SetBytesArgv(&config, 3, (char * const *)argv);

  Py_InitializeFromConfig(&config);
  PyRun_SimpleString("import sys");
  
  // remove last path entry and add the zip file's dep folder based on the current dynamic library path
  PyRun_SimpleString("sys.path.pop()");
  auto mod_zip_path = std::string("sys.path.insert(0, '") + get_mod_zip_path().string() + "')";
  PyRun_SimpleString(mod_zip_path.c_str());
  auto mod_deps_path = std::string("sys.path.insert(0, '") + get_mod_zip_path().string() + "/deps/')";
  PyRun_SimpleString(mod_deps_path.c_str());

  PyRun_SimpleString(
    "from MMGenerate import main as generate\n"
    "generate()"
  );
  
  // finalize python
  Py_Finalize();
}

extern "C" void recomp_main(uint8_t* rdram, recomp_context* ctx) {
  generate();
}
