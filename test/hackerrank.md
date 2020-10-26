# 1. Balanced Array

Given an array of numbers, find the index of the smallest array element (the *pivot*), for which the sums of all elements to the left and to the right are equal. The array may not be reordered.

 

**Example**

*arr=[1,2,3,4,6]*

 

- the sum of the first three elements, *1+2+3=6*. The value of the last element is *6.* 
- Using zero based indexing, *arr[3]=4* is the pivot between the two subarrays.
- The index of the pivot is *3*.

 

**Function Description** 

Complete the function *balancedSum* in the editor below.

 

balancedSum has the following parameter(s):

  int *arr[n]:* an array of integers

Returns:

  int: an integer representing the index of the pivot

 

**Constraints**

- *3 ≤ n ≤ 105*
- *1 ≤ arr[i] ≤ 2 × 104*, where *0 ≤ i < n*
- It is guaranteed that a solution always exists.

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Input Format for Custom Testing</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">Input from stdin will be processed as follows and passed to the function.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The first line contains an integer <em>n</em>, the size of the array <em>arr</em>.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">Each of the next <em>n</em> lines contains an integer, <em>arr[i],</em> where <em>0 ≤ i &lt; n</em>.</p></div></details>

<details open="open" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 0</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Sample Input 0</strong></p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN&nbsp;&nbsp;&nbsp;&nbsp; Function Parameters
-----&nbsp;&nbsp;&nbsp;&nbsp; ------------------- 
4      →&nbsp;&nbsp;arr[] size n = 4
1      →&nbsp;&nbsp;arr = [1, 2, 3, 3] 
2
3
3</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Sample Output 0</strong></p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">2</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Explanation 0</strong></p><ul style="padding-left: 30px;"><li style="font-weight: 400; font-family: var(--font-family-text); margin-bottom: 4px; font-size: 14px; white-space: normal; margin-top: 4px;">The sum of the first two elements,<span>&nbsp;</span><em>1+2=3.</em>&nbsp;The value of the last element is 3<em>.</em>&nbsp;</li><li style="font-weight: 400; font-family: var(--font-family-text); margin-bottom: 4px; font-size: 14px; white-space: normal; margin-top: 4px;">Using zero based indexing,<span>&nbsp;</span><em>arr[2]=3&nbsp;</em>is the pivot between the two subarrays.</li><li style="font-weight: 400; font-family: var(--font-family-text); margin-bottom: 4px; font-size: 14px; white-space: normal; margin-top: 4px;">The index of the pivot is<span>&nbsp;</span><em>2</em>.</li></ul></div></details>

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 1</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Sample Input 1</strong></p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN&nbsp;&nbsp;&nbsp;&nbsp; Function Parameters
-----&nbsp;&nbsp;&nbsp;&nbsp; -------------------
3      →&nbsp;&nbsp;arr[] size n = 3 
1      →&nbsp;&nbsp;arr = [1, 2, 1] 
2
1
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Sample Output 1</strong></p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">1</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Explanation 1</strong></p><ul style="padding-left: 30px;"><li style="font-weight: 400; font-family: var(--font-family-text); margin-bottom: 4px; font-size: 14px; white-space: normal; margin-top: 4px;">The first and last elements are equal to 1<em>.</em>&nbsp;</li><li style="font-weight: 400; font-family: var(--font-family-text); margin-bottom: 4px; font-size: 14px; white-space: normal; margin-top: 4px;">Using zero based indexing,<span>&nbsp;</span><em>arr[1]=2&nbsp;</em>is the pivot between the two subarrays.</li><li style="font-weight: 400; font-family: var(--font-family-text); margin-bottom: 4px; font-size: 14px; white-space: normal; margin-top: 4px;">The index of the pivot is<span>&nbsp;</span><em>1</em>.</li></ul><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p></div></details>

---

# 2. Last and Second-Last

Given a string, create a new string made up of its last two letters, reversed and separated by a space.

 

Example

Given the word '*bat*', return '*t a*'.

 

Function Description

Complete the function *lastLetters* in the editor below.

 

*lastLetters* has the following parameter(s):

  *string word:* a string to process

 

Returns:

  *string: a* string of two space-separated characters

 

Constraint

- *2 ≤* length of *word ≤ 100*

 

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Input Format for Custom Testing</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">Input from stdin will be processed as follows and passed to the function.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The line contains a string, <em>word</em>.</p></div></details>

<details open="open" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 0</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Input</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN     Function
-----     -----
APPLE  →  word = 'APPLE'</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Output</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">E L</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Explanation</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The last letter in '<em>APPLE'</em> is <em>E</em> and the second-to-last letter is <em>L</em>, so return <em>E L</em>.</p></div></details>

---

# 4. Prime or Not?

Given an integer, if the number is prime, return 1. Otherwise return its smallest divisor greater than 1.

 

**Example**

*n = 24* 

 

The number *24* is not prime: its divisors are *[1, 2, 3, 4, 6, 8, 12, 24].* The smallest divisor greater than *1* is *2.*

 

**Function Description** 

Complete the function *isPrime* in the editor below.

 

isPrime has the following parameter(s):

  *long* *n:* a long integer to test

**Returns**

  *int:* if the number is prime, return *1*; otherwise returns the smallest divisor greater than *1*

 

**Constraints**

- *2 ≤ n ≤ 1012*

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Input Format for Custom Testing</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">Input from stdin will be processed as follows and passed to the function.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The only line of input contains the long integer to analyze, <em>n</em>.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p></div></details>

<details open="open" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 0</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Sample Input 0</strong></p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN &nbsp; &nbsp; &nbsp;Function
----- &nbsp; &nbsp; &nbsp;--------
2 &nbsp; &nbsp; &nbsp;→ &nbsp; n = 2
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Sample Output 0</strong></p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">1</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Explanation 0</strong></p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">As <em>2</em> is a prime number, the function returns <em>1</em>.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p></div></details>

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 1</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Sample Input 1</strong></p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Function
----- &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--------
4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→ &nbsp;&nbsp;n = 4
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Sample Output 1</strong></p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">2</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><strong>Explanation 1</strong></p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">Since <em>4</em> is not a prime number, and the factors of 4 are <em>[1, 2, 4],</em> the function returns the smallest factor of <em>4 </em>greater than<em> 1</em>.</p></div></details>

---

# 5. Minimum Start Value

Start with a given array of integers and an arbitrary initial value *x*. Calculate the running sum of *x* plus each array element, from left to right. The running sum must never get below *1.* Determine the minimum value of *x.* 

 

Example

*arr = [-2, 3, 1, -5].* 

 

If *x = 4,* the following results are obtained:

```
Running     
sum       arr[i]
-----     -----
4          -2
2           3
5           1
6          -5
1
```

 

The final value is *1,* and the running sum has never dropped below *1.* The minimum starting value for *x* is 4.

 

Function Description

Complete the function *minX* in the editor below.

 

minX has the following parameter(s):

  *int arr[n]:* an array of integers

 

Returns

  int: the minimum integer value for *x*

 

Constraints

- *1 ≤ n ≤ 105*
- *−100 ≤ arr[i] ≤ 100*

 

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Input Format for Custom Testing</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">Input from stdin will be processed as follows and passed to the function.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The first line contains an integer <em>n</em>, the size of the array <em>arr</em>.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">Each of the next <em>n</em> lines contains an integer <em>arr[i]</em>.</p></div></details>

<details open="open" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 0</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Input</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN     Function
-----     -----
10     →  arr[i] size n = 10
-5     →  arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]
4
-2
3
1
-1
-6
-1
0
5
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Output</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">8</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Explanation</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">Running 
sum       arr[i] 
-----     ----- 
8          -5
3           4
7          -2
5           3
8           1
9          -1
8          -6
2          -1
1           0
1           5
6
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The minimum starting value for <em>x</em> is <em>8</em>.</p></div></details>

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 1</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Input</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN     Function
-----     -----
5      →  arr[i] size n = 5
-5     →  arr = [-5, 4, -2, 3, 1]
4
-2
3
1
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Output</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">6</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Explanation</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">Running 
sum      arr[i] 
-----    ----- 
6         -5
1          4
5         -2
3          3
6          1
7           
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The minimum starting value for <em>x </em>is <em>6.</em></p></div></details>

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 2</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Input</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN     Function
-----     -----
10     →  arr[i] size n = 10
-5     →  arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, -5]
4
-2
3
1
-1
-6
-1
0
-5
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Output</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">13</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Explanation</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">Running 
sum        arr[i] 
-----      ----- 
13          -5
 8           4
12          -2
10           3
13           1
14          -1
13          -6
 7          -1
 6           0
 6          -5
 1
</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The minimum starting value for <em>x </em>is <em>13. </em></p></div></details>

---

# 6. Count String Permutations

Find the number of strings of a given length that can be formed under the following rules:

- Each letter is a vowel, that is, it is in the set *{a, e, i, o, u}*.
- The letter *a* may only be followed by the letter *e*.
- An *e* may only be followed by an *a* or an *i*.
- An *i* may not be next to another *i.*
- The letter *o* may only be followed by an *i* or a *u.*
- The letter *u* may only be followed by an *a.*

 

Example

To illustrate some of the rules, start with the string *s = 'a*' and build to the right.

1. *'a'* may only be followed by '*e'*, so the new string can be *'ae'.*
2. *'ae'* may only be followed by '*a'* or '*i*', so the new string can be '*aea'* or '*aei'*.
3. *'aea'* must be '*aeae'* next, and '*aei'* can be '*aeia', 'aeie', 'aeio',* or '*aeiu'* because an '*i'* cannot follow another '*i'.*

 

Analyses of lengths of strings up to *3* are in the samples below. Since the number of permutations might be very large, return the value modulo *(109 + 7)*.

 

Function Description

Complete the *countPerms* function in the editor below.

 

countPerms has the following parameter(s):

  *int* *n:* the length of string to analyze

 

Returns:

  *int*: the number of permutations, modulo *(109 + 7)*

 

Constraints

- *0 < n < 105*

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Input Format For Custom Testing</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">Input from stdin will be processed as follows and passed to the function.</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">The only line contains an integer, <em>n</em>, the length of the string to analyze.</p></div></details>

<details open="open" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 0</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Input</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN     Function
-----&nbsp;&nbsp;&nbsp;&nbsp; -----
1&nbsp;&nbsp;&nbsp;&nbsp;  →&nbsp;&nbsp;length of string to analyze n = 1</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Output</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">5</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Explanation</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">There are <em>5</em> strings of length <em>1,</em>&nbsp;each containing a single vowel.<em> </em></p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><em>5 mod (10<sup>9</sup>+7) = 5.</em></p></div></details>

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 1</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Input</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN     Function
-----&nbsp;&nbsp;&nbsp;&nbsp; -----
2&nbsp;&nbsp;&nbsp;&nbsp;  →&nbsp;&nbsp;length of string to analyze n = 2</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Output</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">10</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Explanation</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">There are <em>10</em> strings of length <em>2</em>: <em>{'io', 'iu', 'oi', 'ou', 'ua', 'ae', 'ea', 'ei', 'ia', 'ie'}. </em></p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><em>10 mod (10<sup>9</sup>+7) = 10</em></p></div></details>

<details open="" style="background-color: transparent; padding: 0px 4px 2px;"><summary class="section-title" style="background-color: rgb(57, 66, 78); color: white; font-weight: bold; margin-top: 4px; margin-bottom: 4px; padding: 8px;">Sample Case 2</summary><div class="collapsable-details" style="margin: 0px auto; overflow: auto; padding: 0px 4px 2px;"><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Input</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">STDIN     Function
-----&nbsp;&nbsp;&nbsp;&nbsp; -----
3&nbsp;&nbsp;&nbsp;&nbsp;  →&nbsp;&nbsp;length of string to analyze n = 3</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Sample Output</p><pre style="font-weight: 400; font-family: var(--font-family-input); overflow-x: auto; padding: 10px; background-color: rgb(244, 250, 255); color: rgb(57, 66, 78); font-size: 14px; line-height: 20px; border: 0px; border-radius: 2px; margin: 4px;">19</pre><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">&nbsp;</p><p class="section-title" style="font-weight: bold; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px;">Explanation</p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;">There are <em>19</em> strings of length <em>3</em>: <em>{'iua', 'oia', 'oie', 'oio', 'oiu', 'oua', 'uae', 'aea', 'aei', 'eae', 'eia', 'eie', 'eio', 'eiu', 'iae', 'iea', 'iei', 'ioi', 'iou'}. </em></p><p style="font-weight: 400; font-family: var(--font-family-text); margin: 0px; white-space: pre-wrap; padding: 0px 4px 2px;"><em>19 mod (10<sup>9</sup>+7) = 19</em></p></div></details>

