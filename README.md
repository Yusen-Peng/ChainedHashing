# Lab2 -- HashTable with chained hashing

## Author: Yusen Peng

## Data Structure Overview

Hashtable with Chained hashing.
Implemented and tested four kernel methods:

1. init -- initialize a hashtable
2. insert -- insert a key-value pair into the hashtable
3. retrieve -- retrieve the data value based on the given key
4. member -- check if a key is in the hashtable

## Script Files

There are 5 files in this lab:

1. hashtable.py: the kernel implementation of a hashtable using chained hashing
2. developed.py: actual output of test cases using the hashtable I've implemented
3. expected.py: expected output of test cases hardcoded by me
4. benchmark.py: the file to run all test cases of the hashtable
5. util.py: a bunch of utility functions to refactor the test benchmark

## How to Run it

It is really easy. Run the following command in the terminal:

```bash
python3 benchmark.py
```

That's it. this is the only command you need to run.

## Test Output Explanation

Let's grab a piece of test output and explain what's going on.

```txt
This is test case #10
The method being tested: member
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express'), 'member 39']
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
developed return:
True
-----------------------------------------------
expected return:
True
-----------------------------------------------
CONGRATS! test case #10 passed.
```

It's kind of confusing. Let's break it down and explain:

```txt
This is test case #10
The method being tested: member
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express'), 'member 39']
```

the piece of output above explains which test case we are running, the method being tested, the size of the hashtable we are using, and input to the hashtable. The input may contain a variety of data. a ordered pair (key, data) implies the pair we are inserting to the hashtable. "retrieve #" means we are calling retrieve method with key `#`. "member #" means we are invoking member method with key `#`.

```txt
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
```

the piece of output above demenstrates the actual hashtable and the expected hashtable after the method finishes execution. The hashtable is depicted by a list of linkedlists.

```txt
developed return:
True
-----------------------------------------------
expected return:
True
```

the piece of output above demenstrates the actual return value and the expected return value after the method finishes execution. Note that return values are only applicable for retrieve and member methods.

```txt
-----------------------------------------------
CONGRATS! test case #10 passed.
```

the message that says this particular test case has already passed.

## Complete Test Output

the complete test output is attached here:

```txt
This is test case #1
The method being tested: init
The size of the hashtable: 10
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: []
entry3: []
entry4: []
entry5: []
entry6: []
entry7: []
entry8: []
entry9: []
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: []
entry3: []
entry4: []
entry5: []
entry6: []
entry7: []
entry8: []
entry9: []
CONGRATS! test case #1 passed.

This is test case #2
The method being tested: init
The size of the hashtable: 15
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: []
entry3: []
entry4: []
entry5: []
entry6: []
entry7: []
entry8: []
entry9: []
entry10: []
entry11: []
entry12: []
entry13: []
entry14: []
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: []
entry3: []
entry4: []
entry5: []
entry6: []
entry7: []
entry8: []
entry9: []
entry10: []
entry11: []
entry12: []
entry13: []
entry14: []
CONGRATS! test case #2 passed.

This is test case #3
The method being tested: insert
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React')]
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React')]
entry4: []
entry5: []
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React')]
entry4: []
entry5: []
CONGRATS! test case #3 passed.

This is test case #4
The method being tested: insert
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular')]
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React')]
entry4: []
entry5: [(5, 'Angular')]
CONGRATS! test case #4 passed.

This is test case #5
The method being tested: insert
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express')]
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
CONGRATS! test case #5 passed.

This is test case #6
The method being tested: retrieve
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express'), 'retrieve 3']
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
developed return:
React
-----------------------------------------------
expected return:
React
-----------------------------------------------
CONGRATS! test case #6 passed.

This is test case #7
The method being tested: retrieve
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express'), 'retrieve 39']
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
developed return:
Express
-----------------------------------------------
expected return:
Express
-----------------------------------------------
CONGRATS! test case #7 passed.

This is test case #8
The method being tested: retrieve
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express'), 'retrieve 5']
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
developed return:
Angular
-----------------------------------------------
expected return:
Angular
-----------------------------------------------
CONGRATS! test case #8 passed.

This is test case #9
The method being tested: member
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express'), 'member 20']
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
developed return:
True
-----------------------------------------------
expected return:
True
-----------------------------------------------
CONGRATS! test case #9 passed.

This is test case #10
The method being tested: member
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express'), 'member 39']
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
developed return:
True
-----------------------------------------------
expected return:
True
-----------------------------------------------
CONGRATS! test case #10 passed.

This is test case #11
The method being tested: member
The size of the hashtable: 6
The test input: [(20, 'Vue'), (3, 'React'), (5, 'Angular'), (39, 'Express'), 'member 1024']
-----------------------------------------------
developed table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
expected table:
entry0: []
entry1: []
entry2: [(20, 'Vue')]
entry3: [(3, 'React'), (39, 'Express')]
entry4: []
entry5: [(5, 'Angular')]
-----------------------------------------------
developed return:
False
-----------------------------------------------
expected return:
False
-----------------------------------------------
CONGRATS! test case #11 passed.
```