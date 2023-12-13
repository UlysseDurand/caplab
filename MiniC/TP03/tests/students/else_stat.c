#include "printlib.h"

int main(){
  int x; int y;
  x = 42;
  y = 42;
  if (x / y != 1) {
    println_int(0);
  } else {
    println_int(1);
 }
  return 0;
}

// EXPECTED
// 1
