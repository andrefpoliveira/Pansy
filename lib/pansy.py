from lib import errors, strings_with_arrows, lexer, parser, interpreter
from lib.utils import token, nodes

global_symbol_table = interpreter.SymbolTable()
global_symbol_table.set('null', interpreter.Number(0))

#####################
# RUN
#####################
def run(fn, text):
	# Generate tokens
	lex = lexer.Lexer(fn, text)
	tokens, error = lex.make_tokens()
	if error: return None, error

	# Generate AST
	pars = parser.Parser(tokens)
	ast = pars.parse()
	if ast.error: return None, ast.error

	inter = interpreter.Interpreter()
	context = interpreter.Context('<program>')
	context.symbol_table = global_symbol_table
	result = inter.visit(ast.node, context)

	return result.value, result.error