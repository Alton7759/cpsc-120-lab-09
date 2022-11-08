
# Spell Checker

You may have noticed that text entry apps like word processors and social media can check spelling.
Usually they display a misspelled word with red underliniing.

In this exercise, you will create a spell checker program. Your program will scan a *document file* for misspelled
words. It will use a *dictionary file* to determine which words are spelled properly and improperly. For our
purposes, a word counts as spelled properly when it is present in the dictionary file, and counts as misspelled 
when it is absend from the dictionary file.

Your program must:
1. Take the document filename as a command line argument.
1. Validate that the command line argument exists. If too few arguments are given, print out the error message
   ```
   error: you must give a document filename
   ```
   and return a non-zero exit code.
1. Read the words in the dictionary file `words.txt` into a vector.
1. Read the words in the document file into a vector.
1. Compute a list (vector) of document words that are misspelled (meaning absent from the dictionary vector).
1. Print out
   ```
   spelling errors:
   ```
   on its own line, and then each misspelled word on its own line.
1. Return exit code zero.

## Functions

### `ReadWords`

```C++
// Read all the words from the given filename, and return them as a vector
// of strings.
// If the file cannot be opened, return an empty vector.
std::vector<std::string> ReadWords(const std::string& filename)
```

### `InDictionary`

```C++
// Return true if word is present in dictionary, or false otherwise.
// dictionary is intended to be a vector containing all words from a words.txt
// file.
// word is intended to be a string from a document file, that may or may not
// be spelled properly.
bool InDictionary(const std::vector<std::string>& dictionary,
                  const std::string& word)
```

### `MisspelledWords`

```C++
// Return a vector containing all of the misspelled words in document.
// dictionary is intended to be a vector containing all words from a words.txt
// file.
// document is intended to be a vector of all of the words from a document
// file.
std::vector<std::string> MisspelledWords(
    const std::vector<std::string>& dictionary,
    const std::vector<std::string>& document)
```

### `main`

As usual, you need to complete the program's `main` function.

## Example Input and Output

Input validation:
```
$ ./spelling
error: you must give a document filename
```

Misspellings in `120.txt` (the catalog description of CPSC 120A):
```
spelling errors:
Introduction
tasks,
programs;
programs;
assignment;
flow;
input/output;
functions;
Structured
object-oriented
methodologies.
```

There are no misspellings in `fox.txt`, which contains [the quick brown fox...](https://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog) pangram):
```
spelling errors:
```



## Test Cases

As usual, test your program against the test suite below.

1. Input: `120.txt`,
   Output:
   ```
   spelling errors:
   Introduction
   tasks,
   programs;
   programs;
   assignment;
   flow;
   input/output;
   functions;
   Structured
   object-oriented
   methodologies.
   ```
1. Input: `fox.txt`,
   Output:
   ```
   spelling errors:
   ```
1. Input: `leota.txt`,
   Output:
   ```
   spelling errors:
   Serpents
   spiders,
   rat,
   spirits,
   at!
   Rap
   -
   respond.
   Send
   beyond...
   Goblins
   ghoulies
   Halloween,
   tambourine!
   Creepies
   crawlies,
   pond,
   beyond!
   ```   
1. Input: `lincoln.txt`,
   Output:
   ```
   spelling errors:
   Four
   continent,
   nation,
   Liberty,
   equal.
   Now
   war,
   nation,
   dedicated,
   endure.
   We
   battle-field
   war.
   We
   field,
   live.
   It
   this.
   ```

## What to Do

1. With your partner, edit the `spelling.cc` source file using VS Code. Add the required header. Replace all the TODO comments with working code.
1. Your program must use the `ReadWords`, `InDictionary`, and `MisspelledWords` functions. Do not change the prototypes of these functions (name, return type, argument types).
1. Compile your program with the `$ make` shell command. Use the **debug compile error** procedure to debug any compile errors.
1. Run your program with the `$ ./spelling` shell command.
1. Test that your program passes all of the test cases in the test suite above. If your program suffers a runtime error, use the **debug runtime error** procedure to debug the error. If your program does not produce the expected output, use the **debug logic error** procedure to debug the error.
1. Test your program against automated test with the `$ make test` command. Debug any runtime errors or logic errors using the same procedures.
1. Check your header with the `$ make header` shell command. Correct any errors.
1. Check for format errors with the `$ make format` shell command. Correct any errors.
1. Check for lint errors with the `$ make lint` shell command. Correct any errors.
1. After your program passes all of these tests and checks, push your code to GitHub. Use the usual trio of commands: `git add`, `git commit`, and `git push`.

## Next Steps

After you have pushed your code, you are done with this lab. You may ask your TA for permission to sign out and leave.
