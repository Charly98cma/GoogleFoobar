# Google Foobar - Charly98cma

My personal take on the Google Foobar challenges.

## Level 1
### Problem 1 - Re-ID
#### Description

Easy problem.

Solved by generating and storing each prime on a string, returning the
substring (`n` to `n+5`) once we have stored `n+5` digits on the string,
since that's the number we're looking for.

#### Pseudocode
```
algorithm prime_seq_substring is
	input: Index N of first digit on the substring
	output: String of 5 digits of prime numbers

	for each prime in range[2..30000] do
		concat prime to prime_seq
		if length of prime_seq >= N+5 do
			break

	return prime_seq[N..N+5]
```

## Level 2
### Problem 1 - En Route Salute
#### Description

Another easy problem, and I had quite a lot of fun solving this in the least
number of lines. Because... why not?.

Solved by splitting the string by the char `<` and counting the number of times
the char `>` appears on each element of the list.
Then, create a list with the indexes of the list but in descending order, since
the that's the number of times each employee on each section of the list will
face an employee walking on the other direction.

The last leg of the solution is, multiplying each element on the list with it's
corresponding element on the list of indexes (this gives the number of
encounters of each employee) and multiplying this number by two, since each
encounter generates two salutes.

And we return the sum of all this numbers (the total number of salutes of all
employees).


#### Pseudocode
```
algorithms salutes_solution is
	input: String S representing the employees
	output: Number of salutes performed by the employees

	for each section in (S split by '<') do
		concat (number of '>' in section) to sec_list

	index_list := (length of sec_list)..0

	for I in range[0..(length of sec_list)] do
		concat ( (elem I of sec_list) * (elem I of index_list) * 2) to salutes_list

	return sum of elements in salutes_list
```

### Problem 2 - Lovely Lucky Lambs
#### Description
#### Pseudocode
## Level 3
### Problem 1 - Bomb Baby
#### Description
#### Pseudocode
### Problem 2 - Fuel Injection  Perfection
#### Description
#### Pseudocode
### Problem 3 - The Grandest Staircase of Them All
#### Description
#### Pseudocode
## Level 4
### Running with Bunnies (WIP)
#### Description
#### Pseudocode
