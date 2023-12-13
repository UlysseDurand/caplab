#include "printlib.h"

int main(){
  int x;
  if (x) {
    println_int(1);
  } else {
    println_int(0);
  }
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 2: invalid type for If condition: integer
