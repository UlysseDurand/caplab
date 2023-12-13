#include "printlib.h"

int main(){
  int x;
  float y;
  y = 42.0;
  println_int(8 % y);
  return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 7 col 14: invalid type for modulo operands: integer and float
