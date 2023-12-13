#include "printlib.h"

int main(){
  int x;
  for (x = 1; x <= 3; x = x + 1) {
    println_int(x);
  }
  return 0;
}

// EXPECTED
// 1
// 2
// 3
