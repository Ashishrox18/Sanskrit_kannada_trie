seperating aksharas

In this code, we first define the Unicode range for Sanskrit letters, which is [\u0900-\u097F]. We then define the input and output file paths.

We open the input and output files using the with statement, which automatically closes the files when we're done with them. We read the input file line by line using a for loop. For each line, we split it into words using the split() method.

We then process each word by using the re.findall() method to find all Sanskrit letters in the word. We join these letters together to form a new Sanskrit word. We write this Sanskrit word to the output file using the write() method.

Note that this code assumes that the input file is encoded in UTF-8. If your input file uses a different encoding, you should adjust the encoding parameter accordingly.
