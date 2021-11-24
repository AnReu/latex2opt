from texyacc_brace import yacc
from texlex import lexer
from print_tree import print_tree
from tex2conllu import get_conllu


class print_tree_token_only(print_tree):

    def get_children(self, node):
        return node['children']

    def get_node_str(self, node):
        return str(node['token'])

class print_tree_token_and_pos(print_tree):

    def get_children(self, node):
        return node['children']

    def get_node_str(self, node):
        return str(node['token']) + str(node['position'])


example_tex = '\\mathbb{want}\n'
# Lex Example
lexer.input(example_tex)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

# Yacc (Parsing) Example
try:
    result = yacc.parse(example_tex)
    print_tree_token_and_pos(result)
    conllu_format = get_conllu(example_tex, 123)
    print(conllu_format)
except:
    print('Error - Could not parse tex.')