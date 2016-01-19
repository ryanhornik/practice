"""
left, right, and parent should be instances of this class
data should be some order-able type implementing __gt__, __lt__, __ge__, __le__, __eq__
"""


class Node(object):
    left = None
    right = None
    data = None
    parent = None

    def __init__(self, data, parent=None, left=None, right=None):
        if not isinstance(data, tuple):
            data = (data, data)
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def is_root(self):
        return self.parent is None

    def root(self):
        probe = self
        while not probe.is_root:
            probe = probe.parent
        return probe

    @property
    def is_left_child(self):
        return not self.is_root and self.parent.left is self

    @property
    def is_right_child(self):
        return not self.is_root and self.parent.right is self

    @property
    def grandparent(self):
        return None if self.is_root else self.parent.parent

    @grandparent.setter
    def grandparent(self, new_parent):
        self.parent.parent = new_parent

    def is_leaf(self):
        return self.right is None and self.left is None

    '''
    This should be called on x (the element we are accessing)
    This is a single rotation, either right or left
    '''
    def zig(self):
        if self.is_left_child:
            old_parent = self.parent
            self_data = self

            # Make parent equivalent to self
            self.parent.left = self_data.left
            self.parent.right = self_data.right
            self.parent.parent = self_data.parent
            self.parent.data = self_data.data

            self.parent.left = self.right
            self.right = self.parent
        elif self.is_right_child:
            self.parent.right = self.left
            self.left = self.parent

        grandparent = self.grandparent
        self.grandparent = self  # See Phillip J Fry
        self.parent = grandparent

    def zig_zig(self):
        self.parent.zig()
        self.zig()

    def zig_zag(self):
        self.zig()
        self.zig()

    def splay(self):
        while not self.is_root:
            if self.parent.is_root:
                self.zig()
            elif (self.is_left_child and self.parent.is_left_child) or \
                 (self.is_right_child and self.parent.is_right_child):
                self.zig_zig()
            elif (self.is_left_child and self.parent.is_right_child) or \
                 (self.is_right_child and self.parent.is_left_child):
                self.zig_zag()

    def __getitem__(self, key):
        if self.data is None:
            return None
        if self.data[0] == key:
            self.splay()
            return self.data[1]
        if self.data[0] < key:
            return self.right[key]
        else:
            return self.left[key]

    def __setitem__(self, key, value):
        if self.data is None or self.data[0] == key:
            self.data = (key, value)
            self.splay()
        elif self.data[0] < key:
            if self.right is None:
                self.right = Node(value, parent=self)
                self.right.splay()
            else:
                self.right[key] = value
        else:
            if self.left is None:
                self.left = Node(value, parent=self)
                self.right.splay()
            else:
                self.left[key] = value

    def add(self, data):
        key, value = data if isinstance(data, tuple) else data, data
        self.__setitem__(key, value)

