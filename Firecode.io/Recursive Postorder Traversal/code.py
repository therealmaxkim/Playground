post_ordered_list = []
class BinaryTree:
 
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def postorder(self):
        '''
        Questions
        1. Can the tree be empty?
        2. check definition of binary tree - check that it is not a binary search tree. 
        3. min/max amount of nodes in the binary tree?
        4. as a binary tree, is it guaranteed that left/right of each node will exist unless on the bottom level
        
        Observations
        1. post order is a sequence in which tree is given in left, right, root
        2. need a recursive method - need to identify a base case or when the recursive calls should stop. 
        3. we are given a post ordered list and need to add data of each "node" in post order traversal. 
        
        look at the base case: when we are at the last bottom level. How do we know? we check if the left/right are not none because imbalance 
        may exist, where there is a left subtree but no right subtree. The recursive call stops when both left/right are none, meaning that
        we are looking at the bottom most node. 
        '''
        #travel to the left tree
        if self.get_left_child() is not None:
            self.get_left_child().postorder()
        #travel to the right tree
        if self.get_right_child() is not None:
            self.get_right_child().postorder()
        #add the root data to the post ordered list
        post_ordered_list.append(self.get_root_val())

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data