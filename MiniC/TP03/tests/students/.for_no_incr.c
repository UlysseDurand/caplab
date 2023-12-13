#include "printlib.h"

int main(){
  int x;
  for (x = 1; x < 1;) {
    println_int(0);
  }
  println_int(x);
  return 0;
}

// EXPECTED
// 1
