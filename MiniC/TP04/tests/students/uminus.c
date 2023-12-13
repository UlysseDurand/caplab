#include "printlib.h"

int main() {
    int x;
    x = 4;
    println_int(-x);
    return 0;
}
// EXPECTED
// -4
