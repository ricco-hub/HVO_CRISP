// A hello world program in C++

// using ofstream constructors.

#include <iostream>
#include <fstream>
using namespace std;
int main() 
{
  cout << "Hello, World!";
 std::ofstream o("Hello.txt");

  o << "Hello, World\n" << std::endl;
  return 0;
}
