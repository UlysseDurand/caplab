#include "printlib.h"

int main(){
  bool x;
  int y;
  println_int(x + y);
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 14: invalid type for additive operands: boolean and integer
