class Solution(object):
    def inorderTraversal(self, root):
        res = []
        curr = root

        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if not pred.right:      # first visit: create thread
                    pred.right = curr
                    curr = curr.left
                else:                   # second visit: remove thread, visit node
                    pred.right = None
                    res.append(curr.val)
                    curr = curr.right

        return res