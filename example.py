from texyacc_brace import yacc
from texlex import lexer
from print_tree import print_tree


class print_tree_token_only(print_tree):

    def get_children(self, node):
        return node['children']

    def get_node_str(self, node):
        return str(node['token'])


example_tex = 'a \\cdot 2 = \\pi \\cdot 3\n' # tex strings need to end with \n
example_tex = 'dim (KerT^t)+dim (ImT^t)=dim (W\')---(2)\n'
# Lex Example
lexer.input(example_tex)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

# Yacc (Parsing) Example
try:
    result = yacc.parse(example_tex, debug=True)
    print_tree_token_only(result)
except:
    print('Error - Could not parse tex.')