from texyacc_brace import yacc
from texlex import lexer


class SentenceInformation:
    def __init__(self, sentence, id):
        self.tokens = {} # dict: position -> Token
        self.heads = {} # dict: position -> head (parent token position)
        self.sentence = sentence
        self.id = id

    def append_token(self, token):
        if token.type == 'newline':
            return
        self.tokens[token.lexpos] = token

    def add_head(self, position, head):
        if position in self.heads:
            print(f'Warning, {position} already has head! Setting new head {head}.')
        if position == -1:
            return

        self.heads[position] = head

    def set_root(self, position):
        self.add_head(position, 'Root')

    def to_conllu(self):
        all_positions = self.tokens.keys()
        only_heads = [pos for pos in all_positions if pos in self.heads]
        sorted(all_positions)
        pos2idx = {pos: i+1 for i, pos in enumerate(only_heads)}
        pos2idx['Root'] = 0
        info = f'# sent_id = {self.id}\n# text = {self.sentence}'
        for pos in all_positions:
            try:
                idx = pos2idx[pos]
                token_str = self.tokens[pos].value
                type = self.tokens[pos].type
                parent_id = pos2idx[self.heads[pos]]
                info += f'{idx}\t{token_str}\t{token_str}\t{type}\t_\t_\t{parent_id}\t_\t{parent_id}:_\t_\n'
            except:
                #print(pos, self.tokens[pos])
                pass


        return info

    def print_sent_info(self):
        all_positions = self.tokens.keys()
        sorted(all_positions)
        pos2idx = {pos: i+1 for i, pos in enumerate(all_positions)}
        pos2idx['Root'] = 0
        info = ''
        for pos in all_positions:
            idx = pos2idx[pos]
            token_str = self.tokens[pos].value
            type = self.tokens[pos].type
            parent_id = pos2idx[self.heads[pos]]
            info += f'{idx} {token_str} {type} {parent_id}\n'

        print(info)


def add_heads(root, sent_info,last_parent_pos=0):
    for child in root['children']:
        if root['position'] != -1:
            sent_info.add_head(child['position'], root['position'])
            add_heads(child, sent_info, root['position'])
        else:
            print(-1, root)
            exit()
            sent_info.add_head(child['position'], last_parent_pos)
            add_heads(child, sent_info, last_parent_pos)


from print_tree import print_tree
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

def get_conllu(tex, sent_id):

    sent_info = SentenceInformation(tex, sent_id)
    lexer.input(tex)
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        sent_info.append_token(tok)

    parse_result = yacc.parse(tex)
    #print_tree_token_only(parse_result)
    sent_info.set_root(parse_result['position'])



    add_heads(parse_result, sent_info)
    #sent_info.print_sent_info()
    return sent_info.to_conllu()
