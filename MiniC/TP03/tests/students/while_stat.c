#include "printlib.h"

int main(){
  int x; int y;
  x = 3;
  y = 0;
  while (x > y) {
    y = y + 1;
    println_int(y);
  }
  return 0;
}

// EXPECTED
// 1
// 2
// 3
