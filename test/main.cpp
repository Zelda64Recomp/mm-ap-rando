#include <stdio.h>
#include <dlfcn.h>
#include <librecomp/recomp.h>

int main() {
  void* dylib = dlopen("../libMMRecompRando.dylib", RTLD_LAZY);
  if (!dylib) {
    fprintf(stderr, "Error loading dylib: %s\n", dlerror());
  }
  
  void (*recomp_main)(uint8_t*, recomp_context*) = (void (*)(uint8_t*, recomp_context*))dlsym(dylib, "recomp_main");
  if (!recomp_main) {
    fprintf(stderr, "Error loading symbol: %s\n", dlerror());
  }

  recomp_main(nullptr, nullptr);
}
