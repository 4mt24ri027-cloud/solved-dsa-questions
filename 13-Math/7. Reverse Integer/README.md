<h2><a href="https://leetcode.com/problems/reverse-integer">7. Reverse Integer</a></h2>

<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---

# 🛍️ Reverse-Integer | Explained

## Approach 1: Mathematical Digit Extraction and Post-Reversal Boundary Check

### Intuition
Think of a number as a line of shipping boxes moving along a conveyor belt, where each box is labeled with a single digit. To reverse the order, you pick up the last box on the belt, move it over to a new conveyor belt, and push all previously placed boxes one step forward to make room for the new one. 

Mathematically, in base-10 arithmetic:
- Taking modulo $10$ (`x % 10`) pops the units digit off the number.
- Multiplying the accumulator by $10$ shifts all existing digits one position to the left (increasing their place value by a power of 10).
- Integer division by $10$ (`x // 10`) removes the extracted units digit from the original number.

Because standard 32-bit signed integers have strict upper and lower limits, reversing the digits can easily cause the value to exceed those bounds (e.g., `1,534,236,469` reversed becomes `9,646,324,351`, which overflows a signed 32-bit int). In Python, integers have arbitrary precision (they do not overflow automatically into negative values or throw errors). Therefore, we can reverse the integer cleanly first and then validate whether the result falls within the signed 32-bit range $[-2^{31}, 2^{31} - 1]$.

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Input: x]) --> CheckSign{x < 0 ?}
    CheckSign -- Yes --> SetSignNeg[sign = -1, x = |x|]
    CheckSign -- No --> SetSignPos[sign = 1, x = x]
    
    SetSignNeg --> InitAccum[reversed_num = 0]
    SetSignPos --> InitAccum
    
    InitAccum --> LoopCondition{x > 0 ?}
    LoopCondition -- Yes --> Peel[last_digit = x % 10]
    Peel --> Shift[reversed_num = reversed_num * 10 + last_digit]
    Shift --> Truncate[x = x // 10]
    Truncate --> LoopCondition
    
    LoopCondition -- No --> RestoreSign[reversed_num = reversed_num * sign]
    RestoreSign --> BoundCheck{-2^31 <= reversed_num <= 2^31 - 1 ?}
    
    BoundCheck -- Yes --> ReturnResult([Return reversed_num])
    BoundCheck -- No --> ReturnZero([Return 0])
```

### Approach
1. **Define Boundaries:** Store the minimum and maximum 32-bit signed integer values (`-2**31` and `2**31 - 1`).
2. **Handle Negative Values and Sign:** Determine whether $x$ is negative or positive, store this in a variable `sign`, and work exclusively with the absolute value `abs(x)`. This step is critical in Python because the modulo operator `%` on negative numbers produces results consistent with mathematical floor division rather than C-style truncation toward zero (e.g., in Python `-123 % 10` evaluates to `7`, not `-3`).
3. **Reconstruct the Reversed Number:**
   - Initialize `reversed_num = 0`.
   - While $x > 0$:
     - Isolate the least significant digit via `x % 10`.
     - Shift existing digits in `reversed_num` left by multiplying by $10$, and add the isolated digit.
     - Strip the least significant digit from $x$ via floor division `x //= 10`.
4. **Reapply Sign:** Multiply `reversed_num` by `sign`.
5. **Overflow Check:** Check whether `INT_MIN <= reversed_num <= INT_MAX`. If within range, return `reversed_num`; otherwise, return `0`.

### Detailed Code Analysis

```python
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
```
- **Lines 3–4:** Defines standard IEEE 754 / two's complement 32-bit signed limits: $[-2147483648, 2147483647]$.

```python
        sign = -1 if x < 0 else 1   # remember the sign
        x = abs(x)                  # work with a non-negative number
```
- **Lines 5–6:** Normalizes $x$. In Python, negative numbers with modulo behave as:
  $$-123 = (-13 \times 10) + 7 \implies -123 \pmod{10} = 7$$
  By taking `abs(x)`, we guarantee that `x % 10` returns the expected positive units digit ($3$), and `x // 10` cleanly drops it.

```python
        reversed_num = 0
        while x:
            last_digit = x % 10                          # peel off the last digit
            reversed_num = reversed_num * 10 + last_digit  # append it
            x //= 10                                     # drop it from x
```
- **Lines 8–12:** 
  - `reversed_num` starts at `0`.
  - The `while x:` condition evaluates truthiness (equivalent to `while x != 0:`).
  - Iteration example for $x = 123$:
    1. `last_digit = 123 % 10 = 3`, `reversed_num = 0 * 10 + 3 = 3`, `x = 123 // 10 = 12`
    2. `last_digit = 12 % 10 = 2`, `reversed_num = 3 * 10 + 2 = 32`, `x = 12 // 10 = 1`
    3. `last_digit = 1 % 10 = 1`, `reversed_num = 32 * 10 + 1 = 321`, `x = 1 // 10 = 0`
  - Loop terminates as $x = 0$.

```python
        reversed_num *= sign        # restore the sign
```
- **Line 14:** Restores original polarity. If $x$ was initially $-123$, `reversed_num` becomes $-321$.

```python
        # Out of 32-bit range -> return 0
        if INT_MIN <= reversed_num <= INT_MAX:
            return reversed_num
        return 0
```
- **Lines 17–19:** Validates that the newly constructed value fits in a 32-bit signed integer using Python's chained comparison. Returns `0` if it overflows or underflows.

### Code
```python
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1   # remember the sign
        x = abs(x)                  # work with a non-negative number

        reversed_num = 0
        while x:
            last_digit = x % 10                          # peel off the last digit
            reversed_num = reversed_num * 10 + last_digit  # append it
            x //= 10                                     # drop it from x

        reversed_num *= sign        # restore the sign

        # Out of 32-bit range -> return 0
        if INT_MIN <= reversed_num <= INT_MAX:
            return reversed_num
        return 0
```

### Complexity
- **Time:** $O(\log_{10}(|x|))$. The loop runs once for each digit in the input number $x$. For a 32-bit signed integer, the maximum number of decimal digits is $10$ (since $2^{31} - 1 = 2,147,483,647$). Because the number of loop iterations is bounded by a constant ($d \le 10$), the time complexity is effectively **$O(1)$**.
- **Space:** **$O(1)$**. Only a fixed number of integer variables (`INT_MIN`, `INT_MAX`, `sign`, `reversed_num`, `last_digit`) are allocated. Memory usage remains constant regardless of the magnitude of $x$.

---

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **How would you solve this problem in an environment that strictly forbids 64-bit integers (e.g., pure 32-bit C/C++)?**
   - In languages like C/C++, allowing `reversed_num * 10 + last_digit` to execute when `reversed_num` is already near `INT_MAX` triggers undefined behavior (signed integer overflow). 
   - To prevent this, check *before* multiplying:
     - Check if `reversed_num > INT_MAX / 10` or (`reversed_num == INT_MAX / 10` and `last_digit > 7`).
     - Check if `reversed_num < INT_MIN / 10` or (`reversed_num == INT_MIN / 10` and `last_digit < -8`).

2. **Why does Python's division and modulo behave differently for negative numbers compared to C/Java?**
   - Python uses **floor division** ($a // b = \lfloor a / b \rfloor$), which rounds down toward negative infinity. Consequently, the modulo satisfies $a = (a // b) \times b + (a \% b)$, keeping the sign of $a \% b$ the same as the divisor $b$.
   - C and Java use **truncation toward zero**, where $-123 / 10 = -12$ and $-123 \% 10 = -3$. Taking `abs(x)` up front avoids floor division issues entirely in Python.