#include "printlib.h"

int main(){
  int x;
  bool y;
  println_int(x + y);
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 14: invalid type for additive operands: integer and boolean
