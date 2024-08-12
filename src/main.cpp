#include "utils.h"

#include <stdio.h>
#include <dlfcn.h>
#include <Python.h>
#include <librecomp/recomp.h>
#include <filesystem>

void generate() {
  auto dylib_path = get_mod_dylib_path();

  // initialize python
  Py_SetProgramName(L"Generate.py");
  Py_Initialize();
  PyRun_SimpleString("import sys");
  
  // remove last path entry and add the zip file's dep folder based on the current dynamic library path
  PyRun_SimpleString("sys.path.pop()");
  auto mod_zip_path = std::string("sys.path.insert(0, '") + get_mod_zip_path().string() + "')";
  PyRun_SimpleString(mod_zip_path.c_str());
  auto mod_deps_path = std::string("sys.path.insert(0, '") + get_mod_zip_path().string() + "/deps/')";
  PyRun_SimpleString(mod_deps_path.c_str());

  // Set up the arguments for the script
  std::filesystem::path player_files_path = get_mod_folder() / "Players";
  
  // Convert arguments to wide character strings
  std::wstring warg1 = L"Generate.py";
  std::wstring warg2 = L"--player_files_path";
  std::wstring warg3 = std::wstring(player_files_path.u8string().begin(), player_files_path.u8string().end());

  wchar_t* pargv[] = {
    const_cast<wchar_t*>(warg1.c_str()),
    const_cast<wchar_t*>(warg2.c_str()),
    const_cast<wchar_t*>(warg3.c_str())
  };

  PySys_SetArgv(3, pargv);

  PyRun_SimpleString(
    "from Generate import main as generate\n"
    "generate()"
  );
  
  // finalize python
  Py_Finalize();
}

extern "C" void recomp_main(uint8_t* rdram, recomp_context* ctx) {
  generate();
}
