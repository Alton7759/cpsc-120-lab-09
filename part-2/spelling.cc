// Christian Alton bonilla
// CPSC 120-01
// 2022-11-11
// Alton77@csu.fullerton.edu
// @alton7759
//
// Lab 09-02
// Partners: @annavera38
//
// it spells checks
//
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> ReadWords(const std::string& filename) {
  std::vector<std::string> words;
  std::ifstream input_file_stream{filename};
  std::string line_buffer;
  while (input_file_stream.good()) {
    input_file_stream >> line_buffer;
    words.push_back(line_buffer);
  }
  return words;
}

bool InDictionary(const std::vector<std::string>& dictionary,
                  const std::string& word) {
  bool indic = false;

  for (const std::string& check : dictionary) {
    if (word == check) {
      indic = true;
    }
  }

  return indic;
}

std::vector<std::string> MisspelledWords(
    const std::vector<std::string>& dictionary,
    const std::vector<std::string>& document) {
  std::vector<std::string> bad;
  for (const auto& doc : document) {
    if (!InDictionary(dictionary, doc)) {
      bad.push_back(doc);
    }
  }

  return bad;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments(argv, argv + argc);
  if (arguments.size() != 2) {
    std::cout << "error: you must give a document filename";
    return 1;
  }
  arguments.erase(arguments.begin());
  std::string filename{arguments.at(0)};
  std::cout << "spelling errors:\n";
  for (std::string& badwords :
       MisspelledWords(ReadWords("words.txt"), ReadWords(filename))) {
    std::cout << badwords << "\n";
  }
  return 0;
}
