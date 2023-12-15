from abc import ABC, abstractmethod

# Interface comum para componentes


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Objeto individual


class Leaf(Component):
    def operation(self):
        return "Leaf operation"

# Composição de objetos (pode conter Leaf e/ou Composite)


class Composite(Component):
    def _init_(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite operation: {' '.join(results)}"


# Exemplo de uso
leaf1 = Leaf()
leaf2 = Leaf()

composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

composite.operation()  # Saída: 'Composite operation: Leaf operation Leaf operation'
