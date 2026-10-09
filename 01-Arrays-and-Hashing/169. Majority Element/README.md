<h2><a href="https://leetcode.com/problems/majority-element">169. Majority Element</a></h2>

<p>Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.</p>

<p>The majority element is the element that appears more than <code>⌊n / 2⌋</code> times. You may assume that the majority element always exists in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The input is generated such that a majority element will exist in the array.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?

---

# 🛍️ Majority-Element | Explained

## Approach 1: Hash Map Frequency Counting (Two-Pass)

### Intuition
Imagine you are an election official manually counting paper ballots from a ballot box. Each ballot contains a single candidate's name (the numbers in `nums`). To determine the winner, you set up a tally sheet (a hash table/dictionary). 

As you pull each ballot out of the box one by one, you look at your tally sheet:
- If the candidate's name is already listed, you add 1 tick mark to their running total.
- If it is their first time appearing, you write their name down and record 1 tick mark.

Once all the ballots are sorted and tallied, you scan down your completed tally sheet to find the candidate with the highest number of tick marks. Because the problem guarantees that a majority element exists (appearing more than $\lfloor n / 2 \rfloor$ times), the candidate with the maximum tally is guaranteed to be your majority element.

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start: nums array]) --> InitMap[Initialize freq = {}]
    
    subgraph Pass1 [Pass 1: Frequency Accumulation]
        InitMap --> LoopNums{For each num in nums}
        LoopNums -- num exists in freq --> Incr[freq[num] += 1]
        LoopNums -- num not in freq --> Insert[freq[num] = 1]
        Incr --> LoopNums
        Insert --> LoopNums
    end
    
    LoopNums -- Done iterating --> InitMax[Initialize max = 0, max_num = None]
    
    subgraph Pass2 [Pass 2: Find Maximum Frequency]
        InitMax --> LoopDict{For num, count in freq.items}
        LoopDict -- count > max --> UpdateMax[max = count<br>max_num = num]
        LoopDict -- count <= max --> LoopDict
        UpdateMax --> LoopDict
    end
    
    LoopDict -- Done iterating --> ReturnResult([Return max_num])
```

---

### Approach
1. **Initialize a Frequency Map:** Create an empty dictionary `freq` to store each unique number as a key and its total occurrence count as its value.
2. **First Pass (Populate Counts):** Iterate through each integer `i` in the input array `nums`. Check whether `i` already exists as a key in `freq`:
   - If it does, increment its value by `1`.
   - If it does not, initialize its entry with a value of `1`.
3. **Initialize Trackers:** Set a variable `max = 0` to keep track of the highest frequency observed so far.
4. **Second Pass (Find the Dominant Element):** Iterate through the key-value pairs of `freq` using `.items()`. For each `(num, count)` pair:
   - If `count` is strictly greater than `max`, update `max` to `count` and update `max_num` to `num`.
5. **Return Result:** Once the dictionary traversal finishes, return `max_num`.

---

### Detailed Code Analysis

```python
1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
```
- **Lines 1–2:** Defines the standard LeetCode class and method signature. `nums` is accepted as a list of integers, returning an integer representing the majority element.

```python
3        freq = {}
4        for i in nums:
5            if i in freq:
6                freq[i] +=1
7            else:
8                freq[i] = 1
```
- **Line 3:** An empty dictionary `freq` is instantiated. In Python, dictionaries are implemented as hash tables, providing average-case $O(1)$ time complexity for insertions and lookups.
- **Lines 4–8:** A `for` loop inspects each element `i` in `nums`. 
  - `if i in freq:` performs an average $O(1)$ key membership test.
  - If present, `freq[i] += 1` updates the tally.
  - Otherwise, `freq[i] = 1` sets the baseline count for that unique key.

```python
10        max = 0 
11        for num,count in freq.items():
12           if  max < count:
13                max = count 
14                max_num = num 
15
16        return max_num
```
- **Line 10:** `max = 0` initializes the lower bound for frequency tracking. 
  *(Code Review Note: Naming this variable `max` shadows Python's built-in `max()` function. While it works correctly here, renaming it to `max_count` or `highest_freq` is standard practice to avoid overwriting built-in functions).*
- **Lines 11–14:** `freq.items()` returns an iterable view of `(key, value)` tuples. We unpack these into `num` and `count`.
  - The condition `if max < count:` evaluates whether the current number's frequency surpasses our current record.
  - If true, `max` is updated with `count`, and `max_num` is assigned the current `num`.
  - Because a majority element appears strictly more than $\lfloor n/2 \rfloor$ times, no other element can have a frequency equal to or greater than this element. Thus, `max_num` is guaranteed to be set to the true majority element.
- **Line 16:** Returns `max_num`, the element associated with the highest frequency.

---

### Code

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        max = 0 
        for num, count in freq.items():
            if max < count:
                max = count 
                max_num = num 

        return max_num
```

---

### Complexity

- **Time Complexity:** $\mathcal{O}(n)$
  - **Pass 1:** Iterating through `nums` of length $n$ takes $\mathcal{O}(n)$ iterations. Dictionary lookups and insertions operate in $\mathcal{O}(1)$ average time.
  - **Pass 2:** Iterating through `freq.items()` takes $\mathcal{O}(k)$ time, where $k$ is the number of distinct elements in `nums`. Since $k \le n$, the second loop is bounded by $\mathcal{O}(n)$.
  - **Total Time:** $\mathcal{O}(n) + \mathcal{O}(k) = \mathcal{O}(n)$.

- **Space Complexity:** $\mathcal{O}(n)$
  - The dictionary `freq` stores up to $k$ unique elements. In the worst-case scenario where there are many distinct values, $k$ can be up to $n - \lfloor n/2 \rfloor$ unique keys (since one element occupies $> n/2$ spots, the remaining elements can all be unique). Thus, auxiliary memory scales linearly with input size: $\mathcal{O}(n)$.

---

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **How can you optimize this solution to achieve $\mathcal{O}(1)$ auxiliary space?**
   - **Answer:** Use the **Boyer-Moore Voting Algorithm**. Maintain a `candidate` and a `count`. Iterate through `nums`: whenever `count == 0`, assign the current number to `candidate`. Increment `count` if the current number equals `candidate`, else decrement `count`. Because the majority element appears more than $n/2$ times, its count will never be fully canceled out, leaving it as the final candidate in $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space.

2. **Can we terminate the first pass early instead of running two full passes?**
   - **Answer:** Yes. Since the majority element strictly appears more than $\lfloor n / 2 \rfloor$ times, you can check `if freq[i] > len(nums) // 2:` immediately after incrementing the frequency. If this condition is met, you can return `i` immediately, skipping the rest of the array and eliminating the second pass entirely.