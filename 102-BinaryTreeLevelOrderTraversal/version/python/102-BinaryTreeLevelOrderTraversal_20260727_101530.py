# Last updated: 27/07/2026, 10:15:30
1from collections import deque
2from typing import List, Optional
3
4
5class Solution:
6    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
7        if not root:
8            return []
9
10        result = []
11        queue = deque([root])
12
13        while queue:
14            level = []
15
16            for _ in range(len(queue)):
17                node = queue.popleft()
18                level.append(node.val)
19
20                if node.left:
21                    queue.append(node.left)
22                if node.right:
23                    queue.append(node.right)
24
25            result.append(level)
26
27        return result