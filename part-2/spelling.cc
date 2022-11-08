// TODO: add a header

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

// Read all the words from the given filename, and return them as a vector
// of strings.
// If the file cannot be opened, return an empty vector.
std::vector<std::string> ReadWords(const std::string& filename) {
  // TODO: declare an empty vector
  // TODO: open a std::ifstream
  // TODO: write a loop that reads each word from the ifstream, and
  // uses push_back to add each word to the vector
  // TODO: return the vector
  return std::vector<std::string>(); // TODO: replace this return statement with one that actually works
}

// Return true if word is present in dictionary, or false otherwise.
// dictionary is intended to be a vector containing all words from a words.txt
// file.
// word is intended to be a string from a document file, that may or may not
// be spelled properly.
bool InDictionary(const std::vector<std::string>& dictionary,
                  const std::string& word) {
  // TODO: write a linear search loop that determines whether or not
  // word is present in dictionary.
  // TODO: return true if word is present, or false otherwise
  return false; // TODO: replace this return statement with one that actually works
}

// Return a vector containing all of the misspelled words in document.
// dictionary is intended to be a vector containing all words from a words.txt
// file.
// document is intended to be a vector of all of the words from a document
// file.
std::vector<std::string> MisspelledWords(
    const std::vector<std::string>& dictionary,
    const std::vector<std::string>& document) {
  // TODO: declare an empty vector
  // TODO: write a loop that checks each word string in document;
  //   calls InDictionary to determine whether the word is in dictionary;
  //   and adds the word to your vector if it not found
  // TODO: return your vector
  return std::vector<std::string>(); // TODO: replace this return statement with one that actually works}

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);

  // TODO: validate that one argument was provided.
  // If not, print
  // error: you must give a document filename
  // and return a non-zero exit code.

  // TODO: store the first and only command line argument, which holds a
  // document filename, in a variable

  // TODO: call ReadWords to read the contents of words.txt, and store the
  // return value in a variable for the dictionary

  // TODO: call ReadWords to read the contents of the document filename,
  // and store the return value in a variable for the document

  // TODO: call MisspelledWords to find the list of all misspelled words, and
  // store the return value in a variable for the output

  // TODO: print
  // spelling errors:
  // and then use a loop to print out each of the misspelled words

  return 0;
}
