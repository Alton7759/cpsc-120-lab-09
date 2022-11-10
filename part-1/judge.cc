// Christian Alton bonilla
// CPSC 120-01
// 2022-11-09
// Alton77@csu.fullerton.edu
// @alton7759
//
// Lab 09-01
// Partners: @annavera38
//
// Calculate and return the Olympics average of scores.
//
#include <iostream>
#include <string>
#include <vector>

double JudgeAverage(const std::vector<std::string>& scores) {
  double sum{0};
  for (const auto& bruh : scores) {
    sum += std::stod(bruh);
    // std::cout << sum << "sum\n";
  }
  double ave = sum / scores.size();
  // std::cout << scores.size() << "s\n";
  return ave;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);
  double max{0};
  int low_l{0};
  int max_l{0};
  int i{0};
  arguments.erase(arguments.begin());
  if (arguments.size() < 3) {
    std::cout << "error: you must give at least three scores\n";
    return 1;
  }
  double low{std::stod(arguments.at(0))};
  for (const std::string& m : arguments) {
    if (std::stod(m) > max) {
      max = std::stod(m);
      // std::cout << max << "M\n";
      max_l = i;
    }
    i++;
  }
  arguments.erase(arguments.begin() + max_l);
  i = 0;
  for (const std::string& w : arguments) {
    if (std::stod(w) < low) {
      low = std::stod(w);
      // std::cout << low << "L\n";
      low_l = i;
    }
    i++;
  }
  arguments.erase(arguments.begin() + low_l);

  /*for (auto test : arguments) {
    std::cout << test << " ";
  }
  std::cout << "\n" << max_l << "m " << low_l << "l\n";
*/
  std::cout << "average is " << JudgeAverage(arguments) << "\n";

  return 0;
}
