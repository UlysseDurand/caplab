#include "printlib.h"

int main(){
  int x;
  float y;
  println_int(x * y);
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 14: type mismatch for multiplicative operands: integer and float
