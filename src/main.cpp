#include <stdio.h>
#include <librecomp/recomp.h>

void your_method_here() {
  fprintf(stderr, "Hello, World!\n");
}

void recomp_main(uint8_t* rdram, recomp_context* ctx) {
  your_method_here();
}
