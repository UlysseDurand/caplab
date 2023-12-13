#include "printlib.h"

int main(){
  int x; int y;
  x = 42;
  y = 42;
  println_int(4 % (x - y));
  return 0;
}

// SKIP TEST EXPECTED
// EXPECTED
// EXECCODE 1
// Division by 0
