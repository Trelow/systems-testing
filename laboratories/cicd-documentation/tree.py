from node import Node


class Tree:
    """Binary search tree helper class."""

    def __init__(self):
        """Initialize an empty tree (root este `None`)."""
        self.root = None

    # ---------------------------------------------------------------------
    # API public
    # ---------------------------------------------------------------------
    def getRoot(self):
        """Returnează nodul rădăcină al arborelui.

        Returns
        -------
        Node | None
            Nodul rădăcină sau `None` dacă arborele este gol.
        """
        return self.root

    def add(self, data):
        """Adaugă o valoare în arbore (inserare BST).

        Parameters
        ----------
        data : int
            Valoarea de inserat.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def find(self, data):
        """Caută un nod cu valoarea *data*.

        Parameters
        ----------
        data : int
            Valoarea de căutat.

        Returns
        -------
        Node | None
            Nodul găsit sau `None` dacă nu există.
        """
        if self.root is not None:
            return self._find(data, self.root)
        return None

    def deleteTree(self):
        """Şterge tot arborele (setează `root = None`)."""
        self.root = None

    def printTree(self):
        """Printează valorile în in‑ordine (sorted)."""
        if self.root is not None:
            self._printInorderTree(self.root)

    # ---------------------------------------------------------------------
    # API intern (underscore = helper recursive)
    # ---------------------------------------------------------------------
    def _add(self, data, node):
        """Inserare recursivă (helper).

        Parameters
        ----------
        data : int
            Valoarea de inserat.
        node : Node
            Subarborele în care se inserează.
        """
        if data < node.data:
            if node.left:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def _find(self, data, node):
        """Căutare recursivă într‑un subarbore.

        Parameters
        ----------
        data : int
            Valoarea de găsit.
        node : Node
            Rădăcina subarborelui curent.

        Returns
        -------
        Node | None
            Nodul găsit sau `None`.
        """
        if data == node.data:
            return node
        if data < node.data and node.left is not None:
            return self._find(data, node.left)
        if data > node.data and node.right is not None:
            return self._find(data, node.right)
        return None

    # ----------------------- metode de afișare ---------------------------

    def _printInorderTree(self, node):
        """In‑ordine (stânga → nod → dreapta).

        Parameters
        ----------
        node : Node
            Nodul curent din recursie.
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(f"{node.data} ")
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """Pre‑ordine (nod → stânga → dreapta)."""
        if node is not None:
            print(f"{node.data} ")
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """Post‑ordine (stânga → dreapta → nod)."""
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(f"{node.data} ")
