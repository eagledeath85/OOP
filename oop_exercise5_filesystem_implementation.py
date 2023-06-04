class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        before_last_node, directory_name = self._extract_from_path(path)

        new_directory = Directory(directory_name)
        before_last_node.add_node(new_directory)

    def create_file(self, path, contents):
        before_last_node, file_name = self._extract_from_path(path)

        new_file = File(file_name)
        new_file.write_contents(contents)
        before_last_node.add_node(new_file)

    def read_file(self, path):
        before_last_node, file_name = self._extract_from_path(path)

        # Check if the filename is inside before_last_node directory
        if file_name not in before_last_node.children:
            raise ValueError(f"File not found: {file_name}.")

        return before_last_node.children[file_name].contents

    def delete_directory_or_file(self, path):
        before_last_node, node_to_delete = self._extract_from_path(path)

        if node_to_delete not in before_last_node.children:
            raise ValueError(f"Node not found: {node_to_delete}.")

        before_last_node.delete_node(node_to_delete)

    def size(self):
        # Write your code here.
        size = 0
        nodes = [self.root]
        while len(nodes) > 0:
            current_node = nodes.pop()
            if isinstance(current_node, Directory):
                children = list(current_node.children.values())
                nodes.extend(children)
                continue

            if isinstance(current_node, File):
                size += len(current_node)

        return size

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"

    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")

    def _extract_from_path(self, path):
        # Validate path
        FileSystem._validate_path(path)

        # Get node names and new directory name
        path_node_names = path[1:].split("/")
        middle_node_name = path_node_names[:-1]
        last_node_name = path_node_names[-1]

        before_last_node = self._find_bottom_node(middle_node_name)

        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node}is not a directory.")

        return before_last_node, last_node_name

    def _find_bottom_node(self, node_names):
        # Find the folder we want to create the new folder inside of
        current_node = self.root
        for node_name in node_names:
            # Check that current_node is an instance of Directory
            if not isinstance(current_node, Directory):
                raise ValueError(f"{current_node.name} is not a directory.")

            # Check that node_name is in the children of the directory that we're looking at
            if node_name not in current_node.children:
                raise ValueError(f"Value not found: {node_name}")

            current_node = current_node.children[node_name]

        return current_node

class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)
