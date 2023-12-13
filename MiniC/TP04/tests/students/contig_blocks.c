#include "printlib.h"

int main() {
  int x; x=2;
  if (x < 4) {
    x=4;
    println_int(x);
  }
  else {
  }
  return 0;
}

// EXPECTED
// 4
