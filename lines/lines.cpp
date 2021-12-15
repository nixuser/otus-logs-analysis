#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>
using namespace std;

int main () {
  ofstream myfile;
  myfile.open("../lines.log");
  for (int i = 0; i < 100 ; i++) {
    time_t now = time(0);
    myfile << now << ", count: " << i << "\n" << flush;
    this_thread::sleep_for(chrono::milliseconds(1000));
  }
  myfile.close();
  return 0;
}
