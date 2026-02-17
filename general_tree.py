class Tree():
    def __init__(self):
        self.tree = {
            
        }
    
    def add_node(self, node, neighbors):
        self.tree.update({node: neighbors})
        
    def remove_node(self, node):
        self.tree.pop(node)
