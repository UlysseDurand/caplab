from TreeLexer import TreeLexer
from TreeParser import TreeParser
# from AritVisitor import AritVisitor
from MyTreeVisitor import MyTreeVisitor, UnknownIdentifier

from antlr4 import InputStream, CommonTokenStream
import sys

# example of use of visitors to parse arithmetic expressions.
# stops when the first SyntaxError is launched.


def main():
    lexer = TreeLexer(InputStream(sys.stdin.read()))
    stream = CommonTokenStream(lexer)
    parser = TreeParser(stream)

    tree = parser.int_tree_top()
    visitor = MyTreeVisitor()
    is_binary_tree: bool = visitor.visit(tree)
    print("Is it a binary tree ? " + str(is_binary_tree))

if __name__ == '__main__':
    main()
