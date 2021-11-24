import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from texlex import tokens


def p_doc_line_(p):
    'doc : line '
    p[0] = p[1]


def p_doc_doc_line(p):
    'doc : doc line'
    p[0] = {
        "token": "doc",
        "position": p.lexpos(1),
        "children": [p[1], p[2]]}


def p_line_tex_n(p):
    'line : tex newline'
    p[0] = p[1]


def p_tex_term(p):
    'tex : term'
    p[0] = p[1]


def p_tex_tex_ADD_term(p):
    'tex : tex ADD term'
    p[0] = {
        "token": "ADD",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_tex_tex_ADD(p):
    'tex : tex ADD'
    p[0] = {
        "token": "ADD",
        "position": p.lexpos(2),
        "children": [p[1]]}


def p_tex_tex_NEG_term(p):
    'tex : tex NEG term'
    neg_node = {
        "token": "NEG",
        "position": p.lexpos(2),
        "children": [p[3]]}

    p[0] = {
        "token": "ADD",
        "position": -1,
        "neg_position": p.lexpos(2),
        "children": [p[1], neg_node]}


def p_tex_tex_NEG(p):
    'tex : tex NEG'
    p[0] = {
        "token": "tex",
        "position": p.lexpos(1),
        "children": []}


def p_tex_tex_REL_CLASS_tex(p):
    'tex : tex REL_CLASS tex'
    p[0] = {
        "token": "REL_CLASS",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_tex_tex_SEP_CLASS_tex(p):
    'tex : tex SEP_CLASS tex'
    p[0] = {
        "token": "SEP_CLASS",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_tex_tex_ABOVE_tex(p):
    'tex : tex ABOVE tex'
    p[0] = {
        "token": "ABOVE",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_tex_tex__OVER_tex(p):
    'tex : tex _OVER tex'

    p[0] = {
        "token": "FRAC",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_tex_tex_CHOOSE_tex(p):
    'tex : tex CHOOSE tex'
    p[0] = {
        "token": "CHOOSE",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_tex_tex__STACKREL_atom_rel_tex(p):
    'tex : tex _STACKREL atom rel tex'
    p[0] = {
        "token": p[4]['token'],
        "position": p[4]['position'],
        "children": [p[1], p[5]]}


def p_tex_tex__BUILDREL_abv_tex__OVER_rel_tex(p):
    'tex : tex _BUILDREL abv_tex _OVER rel tex'
    p[0] = {
        "token": p[5]['token'],
        "position": p[5]['position'],
        "children": [p[1], p[6]]}


def p_tex_tex__SET_REL_atom_rel_tex(p):
    'tex : tex _SET_REL atom rel tex'
    p[0] = {
        "token": p[4]['token'],
        "position": p[4]['position'],
        "children": [p[1], p[5]]}


def p_tex_tex_X_ARROW_atom_tex(p):
    'tex : tex X_ARROW atom tex'
    p[0] = {
        "token": "X_ARROW",
        "position": p.lexpos(2),
        "children": [p[1], p[4]]}


def p_tex_tex_X_ARROW__L_TEX_BRACKET_abv_tex__R_TEX_BRACKET_atom_tex(p):
    'tex : tex X_ARROW _L_TEX_BRACKET abv_tex _R_TEX_BRACKET atom tex'
    p[0] = {
        "token": "X_ARROW",
        "position": p.lexpos(2),
        "children": [p[1], p[7]]}


def p_rel_atom(p):
    'rel : atom'
    p[0] = {
        "token": "atom",
        "position": p.lexpos(1),
        "children": []}


def p_rel_REL_CLASS(p):
    'rel : REL_CLASS'
    p[0] = {
        "token": "REL_CLASS",
        "position": p.lexpos(1),
        "children": []}


def p_abv_tex_term(p):
    'abv_tex : term'
    p[0] = p[1]


def p_abv_tex_abv_tex_ADD_term(p):
    'abv_tex : abv_tex ADD term'
    p[0] = {
        "token": "ADD",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_abv_tex_abv_tex_ADD(p):
    'abv_tex : abv_tex ADD'
    p[0] = {
        "token": "ADD",
        "position": p.lexpos(2),
        "children": [p[1]]}


def p_abv_tex_abv_tex_NEG_term(p):
    'abv_tex : abv_tex NEG term'

    neg_node = {
        "token": "NEG",
        "position": p.lexpos(2),
        "children": [p[3]]}

    p[0] = {
        "token": "ADD",
        "position": -1,
        "implicit": True,
        "neg_position": p.lexpos(2),
        "children": [p[1], neg_node]}


def p_abv_tex_abv_tex_NEG(p):
    'abv_tex : abv_tex NEG'
    p[0] = p[1]


def p_abv_tex_abv_tex_REL_CLASS_abv_tex(p):
    'abv_tex : abv_tex REL_CLASS abv_tex'
    p[0] = {
        "token": "REL_CLASS",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_abv_tex_abv_tex_SEP_CLASS_abv_tex(p):
    'abv_tex : abv_tex SEP_CLASS abv_tex'
    p[0] = {
        "token": "SEP_CLASS",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_mat_tex_term(p):
    'mat_tex : term'
    p[0] = p[1]


def p_mat_tex_mat_tex_ADD_term(p):
    'mat_tex : mat_tex ADD term'
    p[0] = {
        "token": "ADD",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_mat_tex_mat_tex_ADD(p):
    'mat_tex : mat_tex ADD'
    p[0] = {
        "token": "ADD",
        "position": p.lexpos(2),
        "children": [p[1]]}


def p_mat_tex_mat_tex_NEG_term(p):
    'mat_tex : mat_tex NEG term'

    neg_node = {
        "token": "NEG",
        "position": p.lexpos(2),
        "children": [p[3]]}

    p[0] = {
        "token": "ADD",
        "position": -1,
        "neg_position": p.lexpos(2),
        "implicit": True,
        "children": [p[1], neg_node]}


def p_mat_tex_mat_tex_NEG(p):
    'mat_tex : mat_tex NEG'
    p[0] = p[1]


def p_mat_tex_mat_tex_SEP_CLASS_mat_tex(p):
    'mat_tex : mat_tex SEP_CLASS mat_tex'
    p[0] = {
        "token": "SEP_CLASS",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_mat_tex_mat_tex_ABOVE_mat_tex(p):
    'mat_tex : mat_tex ABOVE mat_tex'
    p[0] = {
        "token": "ABOVE",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_mat_tex_mat_tex__OVER_mat_tex(p):
    'mat_tex : mat_tex _OVER mat_tex'

    p[0] = {
        "token": "FRAC",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_mat_tex_mat_tex_TAB_ROW_mat_tex(p):
    'mat_tex : mat_tex TAB_ROW mat_tex'
    p[0] = {
        "token": "TAB_ROW",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_mat_tex_mat_tex_TAB_COL_mat_tex(p):
    'mat_tex : mat_tex TAB_COL mat_tex'
    p[0] = {
        "token": "TAB_COL",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_term_term_factor(p):
    'term : term factor'

    p[0] = {
        "token": "TIMES",
        "position": -1,
        "implicit": True,
        "children": [p[1], p[2]]}


def p_term_term_TIMES_factor(p):
    'term : term TIMES factor'
    p[0] = {
        "token": "TIMES",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_term_term_DIV_factor(p):
    'term : term DIV factor'
    p[0] = {
        "token": "DIV",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_factor_pack(p):
    'factor : pack'
    p[0] = p[1]


def p_factor_factor_FACT(p):
    'factor : factor FACT'
    p[0] = {
        "token": "FACT",
        "position": p.lexpos(2),
        "children": [p[1]]}


def p_factor_factor_PRIME(p):
    'factor : factor PRIME'
    p[0] = {
        "token": "PRIME",
        "position": p.lexpos(2),
        "children": [p[1]]}


def p_factor_factor_script(p):
    'factor : factor script'

    base = {
        "token": "BASE",
        "position": -1,
        "implicit": True,
        "children": [p[1]]}

    p[2]["children"].append(base)

    p[0] = p[2]


def p_pack_atom(p):
    'pack : atom'
    p[0] = p[1]


def p_pack_pair(p):
    'pack : pair'
    p[0] = p[1]


def p_pack__BEGIN_MAT_mat_tex__END_MAT(p):
    'pack : _BEGIN_MAT mat_tex _END_MAT'
    p[0] = p[2]


def p_atom_VAR(p):
    'atom : VAR'
    p[0] = {
        "token": "VAR",
        "position": p.lexpos(1),
        "children": []}


def p_atom_INFTY(p):
    'atom : INFTY'
    p[0] = {
        "token": "VAR",
        "position": p.lexpos(1),
        "children": []}



def p_atom_SINGLE_LETTER(p):
    'atom : SINGLE_LETTER'
    p[0] = {
        "token": "VAR",
        "position": p.lexpos(1),
        "children": []}

def p_atom_NUM(p):
    'atom : NUM'
    p[0] = {
        "token": "NUM",
        "position": p.lexpos(1),
        "children": []}


def p_atom__L_TEX_BRACE_tex__R_TEX_BRACE(p):
    'atom : _L_TEX_BRACE tex _R_TEX_BRACE'

    p[0] = p[2]


def p_atom_FUN_CLASS(p):
    'atom : FUN_CLASS'
    p[0] = {
        "token": "FUN_CLASS",
        "position": p.lexpos(1),
        "children": []}


def p_atom_SUM_CLASS(p):
    'atom : SUM_CLASS'
    p[0] = {
        "token": "SUM_CLASS",
        "position": p.lexpos(1),
        "children": []}


def p_atom_FRAC__(p):
    'atom : FRAC__'
    p[0] = {
        "token": "FRAC__",
        "position": p.lexpos(1),
        "children": []}


def p_atom_FRAC_atom_atom(p):
    'atom : FRAC atom atom'
    p[0] = {
        "token": "FRAC",
        "position": p.lexpos(1),
        "children": [p[2], p[3]]}


def p_atom_BINOM__(p):
    'atom : BINOM__'
    p[0] = {
        "token": "BINOM__",
        "position": p.lexpos(1),
        "children": []}


def p_atom_BINOM_atom_atom(p):
    'atom : BINOM atom atom'
    p[0] = {
        "token": "BINOM",
        "position": p.lexpos(1),
        "children": [p[2], p[3]]}


def p_atom_VECT_atom(p):
    'atom : VECT atom'
    p[0] = {
        "token": "VECT",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_atom_SQRT_atom(p):
    'atom : SQRT atom'
    p[0] = {
        "token": "SQRT",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_atom_SQRT__L_TEX_BRACKET_tex__R_TEX_BRACKET_atom(p):
    'atom : SQRT _L_TEX_BRACKET tex _R_TEX_BRACKET atom'
    p[0] = {
        "token": "SQRT",
        "position": p.lexpos(1),
        "children": [p[5], p[3]]}


def p_atom_ROOT_atom__OF_atom(p):
    'atom : ROOT atom _OF atom'
    p[0] = {
        "token": "ROOT",
        "position": p.lexpos(1),
        "children": [p[4], p[2]]}


def p_atom_atom_MODULAR_atom(p):
    'atom : atom MODULAR atom'
    p[0] = {
        "token": "MODULAR",
        "position": p.lexpos(2),
        "children": [p[1], p[3]]}


def p_atom__QVAR_VAR(p):
    'atom : _QVAR VAR'

    p[0] = {
        "token": "VAR",
        "position": p.lexpos(2),
        "children": []}


def p_atom__QVAR__L_TEX_BRACE_VAR__R_TEX_BRACE(p):
    'atom : _QVAR _L_TEX_BRACE VAR _R_TEX_BRACE'

    p[0] = {
        "token": "VAR",
        "position": p.lexpos(3),
        "children": []}


def p_s_atom_atom(p):
    's_atom : atom'
    p[0] = p[1]


def p_s_atom_ADD(p):
    's_atom : ADD'

    p[0] = {
        "token": "ADD",
        "position": p.lexpos(1),
        "children": []}


def p_s_atom_NEG(p):
    's_atom : NEG'

    p[0] = {
        "token": "NEG",
        "position": p.lexpos(1),
        "children": []}


def p_s_atom_TIMES(p):
    's_atom : TIMES'

    p[0] = {
        "token": "TIMES",
        "position": p.lexpos(1),
        "children": []}


def p_script_SUBSCRIPT_s_atom(p):
    'script : SUBSCRIPT s_atom'

    p[1] = {
        "token": "SUBSCRIPT",
        "position": p.lexpos(1),
        "children": [p[2]]}

    p[0] = {
        "token": "HANGER",
        "position": -1,
        "implicit": True,
        "children": [p[1]]}


def p_script_SUPSCRIPT_s_atom(p):
    'script : SUPSCRIPT s_atom'

    p[1] = {
        "token": "SUPSCRIPT",
        "position": p.lexpos(1),
        "children": [p[2]]}

    p[0] = {
        "token": "HANGER",
        "position": -1,
        "implicit": True,
        "children": [p[1]]}


def p_script_SUBSCRIPT_s_atom_SUPSCRIPT_s_atom(p):
    'script : SUBSCRIPT s_atom SUPSCRIPT s_atom'

    p[1] = {
        "token": "SUBSCRIPT",
        "position": p.lexpos(1),
        "children": [p[2]]}

    p[3] = {
        "token": "SUPSCRIPT",
        "position": p.lexpos(3),
        "children": [p[4]]}

    p[0] = {
        "token": "HANGER",
        "position": -1,
        "implicit": True,
        "children": [p[1], p[3]]}


def p_script_SUPSCRIPT_s_atom_SUBSCRIPT_s_atom(p):
    'script : SUPSCRIPT s_atom SUBSCRIPT s_atom'

    p[1] = {
        "token": "SUPSCRIPT",
        "position": p.lexpos(1),
        "children": [p[2]]}

    p[3] = {
        "token": "SUBSCRIPT",
        "position": p.lexpos(3),
        "children": [p[4]]}

    p[0] = {
        "token": "HANGER",
        "position": -1,
        "implicit": True,
        "children": [p[1], p[3]]}


def p_pair__L_BRACKET_tex__R_BRACKET(p):
    'pair : _L_BRACKET tex _R_BRACKET'

    p[0] = p[2]


def p_pair__L_DOT_tex__R_BRACKET(p):
    'pair : _L_DOT tex _R_BRACKET'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_BRACKET_tex__R_DOT(p):
    'pair : _L_BRACKET tex _R_DOT'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_BRACKET_tex__R_TEX_BRACKET(p):
    'pair : _L_BRACKET tex _R_TEX_BRACKET'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_TEX_BRACKET_tex__R_BRACKET(p):
    'pair : _L_TEX_BRACKET tex _R_BRACKET'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_ANGLE_tex__R_ANGLE(p):
    'pair : _L_ANGLE tex _R_ANGLE'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_SLASH_tex__R_SLASH(p):
    'pair : _L_SLASH tex _R_SLASH'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_HAIR_tex__R_HAIR(p):
    'pair : _L_HAIR tex _R_HAIR'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_ARROW_tex__R_ARROW(p):
    'pair : _L_ARROW tex _R_ARROW'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_TEX_BRACKET_tex__R_TEX_BRACKET(p):
    'pair : _L_TEX_BRACKET tex _R_TEX_BRACKET'

    p[0] = {
        "token": "GROUP",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_CEIL_tex__R_CEIL(p):
    'pair : _L_CEIL tex _R_CEIL'

    p[0] = {
        "token": "CEIL",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_FLOOR_tex__R_FLOOR(p):
    'pair : _L_FLOOR tex _R_FLOOR'

    p[0] = {
        "token": "FLOOR",
        "position": p.lexpos(1),
        "children": [p[2]]}


def p_pair__L_VERT_tex__R_VERT(p):
    'pair : _L_VERT tex _R_VERT'

    p[0] = {
        "token": "VERTS",
        "position": p.lexpos(1),
        "children": [p[2]]}


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()