
class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """

    def sortedArrayToBST(self, A):
        return self.convert(A, 0, len(A) - 1)

    def convert(self, A, start, end):
        if start > end:
            return None

        if start == end:
            return TreeNode(A[start])

        mid = (start + end) / 2
        root = TreeNode(A[mid])
        root.left = self.convert(A, start, mid - 1)
        root.right = self.convert(A, mid + 1, end)
        return root