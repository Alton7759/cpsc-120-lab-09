
# Olympic Judge Average

In some Olympics events, such as figure skating, scores are determined by judges.
To keep the judging fair, there are several judges. Each judge assigns a score,
and all of the scores are averaged together by an algorithm that is intended to
eliminate impartial scores. This exercise involves writing a function that computes
this kind of average.

[The averaging algorithm](https://www.usfigureskating.org/about/scoring-system) is:
1. at least three judges choose a numerical score (for example, figure skating is on a scale of 0.0 to 6.0);
1. the least (minimum) score is eliminated
1. the greatest (maximum) score is eliminated
1. the remaining scores are averaged together, using the *mean average:*

$$ \frac{1}{n} \sum_{i=1}^n a_i .$$

In words, the mean average is the total of the remaining scores, divided by the count of those scores.

Eliminating the least and greatest scores is intended to achieve fairness by preventing a biased judge
from affecting the final score. If a judge has it out for a particular contestant for some reason, such as bigotry,
and assigns an unfairly low score, it will probably be the low score that gets eliminated. Likewise,
if a judge is trying to elevate someone for some reason, such as a bribe, and assigns an unfairly
high score, it will be the maximum that gets eliminated.

For example:
1. five judges assign scores: 5.8, 5.6, 5.7, 5.9, 5.8
1. eliminate the least score of 5.6: 5.8, ~~5.6,~~ 5.7, 5.9, 5.8
1. eliminate the greatest score of 5.9: 5.8, ~~5.6,~~ 5.7, ~~5.9,~~ 5.8
1. the remaining scores are averaged together: $(5.8 + 5.7 + 5.8) \div 3 = (17.3) \div 3 \approx 5.767$

Your program must:
1. Take the judge scores as command line arguments.
1. Validate that there are at least three scores. If too few arguments are given, print an error message and return a non-zero exit code.
1. Compute the Olympic average as described above.
1. Use floating point arithmetic (`double` or `float` types) so that fractional scores are handled accurately.
1. Print an output message in the form
   ```
   average is *Olympic average*
   ```
1. Return exit code zero.

## Functions

### `JudgeAverage`

```C++
// Calculate and return the Olympics average of scores.
// The return value is the mean of all elements of scores, except for the
// minimum and maximum elements.
double JudgeAverage(const std::vector<double>& scores)
```

### `main`

As usual, you need to complete the program's `main` function.

## Example Input and Output

```
$ ./judge
error: you must give at least three scores
```

```
$ ./judge 1 2
error: you must give at least three scores
```

```
$ ./judge 1 2 3
average is 2
```
(↑ the 1 and 3 are eliminated)

```
$ ./judge 5.1 8.7 9.0 2.6 1.9
average is 5.46667
```
(↑ the 1.9 and 9.0 are eliminated)


```
$ ./judge 4 2 9 9 3
average is 5.33333
```
(↑ the 2, and one of the 9s, are elminiated)

## Test Cases

As usual, test your program against the test suite below.

| Test Case | Input                              | Expected Output                                                       |
|-----------|------------------------------------|-----------------------------------------------------------------------|
| 1         | (no arguments")            | `error: you must give at least three scores`        |
| 2         | 1 2             | `error: you must give at least three scores`        |
| 3         | 1 2 3      | `average is 2` |
| 4         | 5.1 8.7 9.0 2.6 1.9          | `average is 5.46667`  |
| 5         | 4 2 9 9 3             | `average is 5.33333`     |

## What to Do

1. With your partner, edit the `judge.cc` source file using VS Code. Add the required header. Replace all the TODO comments with working code.
1. Your program must use the `JudgeAverage` function. Do not change the prototypes of this function (name, return type, argument types).
1. Compile your program with the `$ make` shell command. Use the **debug compile error** procedure to debug any compile errors.
1. Run your program with the `$ ./judge` shell command.
1. Test that your program passes all of the test cases in the test suite above. If your program suffers a runtime error, use the **debug runtime error** procedure to debug the error. If your program does not produce the expected output, use the **debug logic error** procedure to debug the error.
1. Test your program against automated test with the `$ make test` command. Debug any runtime errors or logic errors using the same procedures.
1. Check your header with the `$ make header` shell command. Correct any errors.
1. Check for format errors with the `$ make format` shell command. Correct any errors.
1. Check for lint errors with the `$ make lint` shell command. Correct any errors.
1. After your program passes all of these tests and checks, push your code to GitHub. Use the usual trio of commands: `git add`, `git commit`, and `git push`.

## Next Steps

After you have pushed your code, move on to part 2.
