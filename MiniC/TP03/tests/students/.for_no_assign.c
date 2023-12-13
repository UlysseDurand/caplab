#include "printlib.h"

int main(){
  int x;
  for (; x <= 2; x = x + 1) {
    println_int(x);
  }
  return 0;
}

// EXPECTED
// 0
// 1
// 2
