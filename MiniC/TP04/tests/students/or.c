#include "printlib.h"

int main() {
    bool x;
    bool y;
    bool z;
    y = true;
    println_bool(x || y);
    println_bool(x || z);
    return 0;
}
// EXPECTED
// 1
// 0
