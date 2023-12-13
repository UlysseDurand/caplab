#include "printlib.h"

int main(){
  int x,y;
  x = 8;
  y = 3;
  println_int(x % 3);
  return 0;
}

// EXPECTED
// 2
