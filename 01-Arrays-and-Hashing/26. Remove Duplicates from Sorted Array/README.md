<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">26. Remove Duplicates from Sorted Array</a></h2>

<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears only <strong>once</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Consider the number of <em>unique elements</em> in&nbsp;<code>nums</code> to be <code>k<strong>​​​​​​​</strong></code>​​​​​​​. After removing duplicates, return the number of unique elements&nbsp;<code>k</code>.</p>

<p>The first&nbsp;<code>k</code>&nbsp;elements of&nbsp;<code>nums</code>&nbsp;should contain the unique numbers in <strong>sorted order</strong>. The remaining elements beyond index&nbsp;<code>k - 1</code>&nbsp;can be ignored.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>


---

# 🛍️ Remove-Duplicates-from-Sorted-Array | Explained

## Approach 1: Two Pointers (Read & Write Pointers)

### Intuition
Imagine a conveyor belt at a grocery store checkout where identical items are grouped together. You have an inspector (the **read pointer**) scanning every item moving along the belt, and a packer (the **write pointer**) who places unique items into the customer's grocery cart. 

Because the items are already sorted, all duplicates are physically adjacent to each other. The inspector compares the current item to the one immediately before it. If it is identical, the inspector skips it. The moment the inspector sees a brand-new item that differs from the previous one, the packer records it at the next available position in the cart. This guarantees that only unique values are written forward, modifying the array completely in place without needing an extra cart (no additional memory).

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start: nums is sorted]) --> CheckEmpty{Is nums empty?}
    CheckEmpty -- Yes --> ReturnZero[Return 0]
    CheckEmpty -- No --> Init[Initialize write_idx = 1<br/>read_idx = 1]
    
    Init --> LoopCheck{read_idx < len nums?}
    LoopCheck -- No --> Finish[Return write_idx]
    
    LoopCheck -- Yes --> Compare{nums[read_idx] != nums[read_idx - 1]?}
    Compare -- No Duplicate Found --> IncrementRead[read_idx += 1]
    Compare -- Yes Unique Found --> Write[nums[write_idx] = nums[read_idx]<br/>write_idx += 1]
    
    Write --> IncrementRead
    IncrementRead --> LoopCheck
```

### Approach
1. **Edge Case Handling**: If the input array `nums` is empty, return `0` immediately.
2. **Pointer Initialization**:
   - The first element (`nums[0]`) is always unique by definition.
   - Initialize a write pointer `write_idx = 1` pointing to the position where the next unique value should be placed.
3. **Array Traversal**:
   - Iterate through the array with a read pointer `read_idx` starting from index `1` to `len(nums) - 1`.
   - At each step, compare `nums[read_idx]` with `nums[read_idx - 1]`.
4. **In-Place Update**:
   - If `nums[read_idx] != nums[read_idx - 1]`, a new distinct element has been found.
   - Overwrite the value at `nums[write_idx]` with `nums[read_idx]`.
   - Increment `write_idx` by `1`.
5. **Result**:
   - Once traversal completes, `write_idx` represents the number of unique elements ($k$), and the first `write_idx` elements of `nums` contain the deduplicated values.

### Detailed Code Analysis
- `if not nums: return 0`: Defensive check to handle empty inputs gracefully.
- `write_idx = 1`: The first element at index `0` is always the first unique element. We start overwriting from index `1`.
- `for read_idx in range(1, len(nums)):`: Scans linearly from the second element to the end.
- `if nums[read_idx] != nums[read_idx - 1]:`: Leverages the sorted property. Duplicates must be contiguous, so checking whether the current element differs from its predecessor is sufficient to detect a transition to a new unique number.
- `nums[write_idx] = nums[read_idx]`: Copies the newly discovered unique value into the next available slot in the modified prefix of the array.
- `write_idx += 1`: Advances the boundary of unique elements.
- `return write_idx`: Returns the length of the deduplicated prefix.

### Code
```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write_idx = 1
        for read_idx in range(1, len(nums)):
            if nums[read_idx] != nums[read_idx - 1]:
                nums[write_idx] = nums[read_idx]
                write_idx += 1

        return write_idx
```

### Complexity
- **Time:** $\mathcal{O}(N)$, where $N$ is the number of elements in `nums`. We scan the array with a single pass using the read pointer, executing constant-time $\mathcal{O}(1)$ operations per element.
- **Space:** $\mathcal{O}(1)$. The algorithm runs strictly in place, using only two integer pointer variables (`write_idx` and `read_idx`) without allocating any auxiliary memory.

---

## 🕵️‍♂️ Follow-up Questions

1. **What if elements are allowed to appear at most twice instead of once (LeetCode 80: Remove Duplicates from Sorted Array II)?**
   - **Answer**: Instead of comparing `nums[read_idx]` to `nums[read_idx - 1]`, we compare `nums[read_idx]` to `nums[write_idx - 2]`. If `nums[read_idx] != nums[write_idx - 2]`, it means the candidate element has not yet appeared two times in the result array, so we can safely assign `nums[write_idx] = nums[read_idx]` and increment `write_idx`. This generalizes to allowing at most $k$ duplicates by checking `nums[write_idx - k]`.

2. **What if the array was not sorted initially?**
   - **Answer**: If the array is unsorted and in-place $\mathcal{O}(1)$ space is strictly required, we would have to sort it first in $\mathcal{O}(N \log N)$ time before applying this two-pointer technique. If extra space is permitted, we can maintain a Hash Set to track seen elements in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space while using a write pointer to compact the array in place.