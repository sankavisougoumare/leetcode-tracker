# Last updated: 23/07/2026, 11:00:14
class Solution:
    def inorderTraversal(self, root):
        ans = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans