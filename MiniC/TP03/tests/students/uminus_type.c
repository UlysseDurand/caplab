#include "printlib.h"

int main(){
  bool x;
  println_int(-x);
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 14: invalid type for Unary Minus operand: boolean
