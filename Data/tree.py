class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
       if self.left_child is None:
            self.left_child = BinaryTree(next_value)
       else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
       return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    #Префиксный
    def pre_order_pr(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order_pr()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order_pr()  # рекурсивно вызываем функцию

    #Постфиксный
    def post_order_po(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order_po()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order_po()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

    #Инфиксный
    def in_order_if(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order_if()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order_if()  # рекурсивно вызываем функцию

# создаём корень и его потомков /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)


node_root.pre_order_pr()
print()
node_root.post_order_po()
print()
node_root.in_order_if()