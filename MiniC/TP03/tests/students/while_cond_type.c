#include "printlib.h"

int main(){
  string x;
  while (x) {
    println_int(1);
  }
  return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 2: invalid type for While condition: string
