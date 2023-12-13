#include "printlib.h"

int main(){
  int x;
  bool y;
  println_bool(x && y);
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 15: invalid type for And operands: integer and boolean
