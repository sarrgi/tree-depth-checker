## Tree Evaluator

Simple program made for assisting in the evaluation of tree like equations, such as individuals generated in Genetic Programming algorithms. Formats the equation into a more readable tree like structure, as well as providing the maximum depth of the tree. Has the  flexibility to be adjusted to evaluate differently formatted equations.

Must be given the file path of the program to evaluate as the first argument. Will print the program evaluation into the console, as well as write the evaluation to a file (output.txt by default).

### Program Run Examples

1.  #### Input
    ```
    mul(add(4,3,8), sub(5, div(4,1)))
    ```
    #### Output
    ```
    -> mul
       -> add
          -> 4
          -> 3
          -> 8
       -> sub
          -> 5
          -> div
             -> 4
             -> 1
    Depth: 2
    ```
2. #### Input
    ```
    b[c[9,a[4,5,6],4], c[9,5,c[9,a[3,4],a[1,2]]]]
    ```
    #### Output
    ```
    -> b
       -> c
          -> 9
          -> a
             -> 4
             -> 5
             -> 6
          -> 4
       -> c
          -> 9
          -> 5
          -> c
             -> 9
             -> a
                -> 3
                -> 4
             -> a
                -> 1
                -> 2
    Depth: 3
    ```


#### Default Parameter Settings:

| Parameter            | Value         |
|:---------------------|:--------------|
| Output file          | output.txt    |
| Separator            | ,             |
| Left Node Indicator  | (             |   
| Right Node Indicator | )             |
| Indent Style         | ->            |


#### Optional Command Line Arguments:

| Parameter            | Aliases                 |
|:---------------------|:------------------------|
| Output file          | f, file, file_name      |
| Separator            | s, sep, separator       |
| Left Node Indicator  | l, left, left_paren,    |   
| Right Node Indicator | r, right, right_paren,  |
| Indent Style         | i, indent, indent_style |


#### Example Command Line Runs:
```
python depth.py tree.txt
```
```
python depth.py path/to/tree.txt l=[ right=) indent_style=--> f=eval_out.txt
```
