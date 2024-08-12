#include <stdio.h>
#include <librecomp/recomp.h>

void generate() {
  fprintf(stderr, "Hello, World!\n");
}

extern "C" void recomp_main(uint8_t* rdram, recomp_context* ctx) {
  generate();
}
