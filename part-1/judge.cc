// TODO: add a header

#include <iostream>
#include <string>
#include <vector>

// Calculate and return the Olympics average of scores.
// The return value is the mean of all elements of scores, except for the
// minimum and maximum elements.
double JudgeAverage(const std::vector<double>& scores) {
  // TODO: write statements to implement this function, and delete this comment
  // Hint:
  // - Write a loop that finds the minimum score.
  // - Write another loop that finds the maximum score.
  // - Write another loop that computes the total of all of the elements.
  // - Subtract the minimum and maximum from the total.
  // - Divide by the number of remaining elements.
  //   (The minimum and maximum don't count.)
  return 0.0; // TODO: replace this return statement with one that actually works
}

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);

  // TODO: validate that at least three arguments were provided.
  // If not, print
  // error: you must give at least three scores
  // and return a non-zero exit code.

  // TODO: Create a vector of doubles that will work as the scores argument
  // for the JudgeAverage function.
  // Use the Build a Vector pattern to write code that:
  //  - declares an empty vector of doubles
  //  - uses a loop to convert each argument to a double/float number, and
  //    use push_back to add the number to the back of the vector
  //  - the loop needs to skip the first element of arguments, which contains
  //    the command name "./judge"

  // TODO: Call the JudgeAverage function to calculate the average.
  // Store the return value of the function in a variable.

  // TODO: Use std::cout to print a message of the form
  // average is *the return value*

  return 0;
}
