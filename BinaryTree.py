# 树的遍历
# 深度优先遍历：前序，中序，后序
# 广度优先遍历

# 树的定义
'''
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''

#深度优先遍历-前序遍历

#递归
class Solution(object):
    def preorderTraversal(self, root):
        if root:
            print(root.val)     
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
#非递归
def preorderTraversal(self, root):
        if not root:
            return None
        stack = [root]
        out = []
        while stack:
            node = stack.pop()
            out.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return out
