from lib import errors, strings_with_arrows, lexer, parser, interpreter
from lib.utils import token, nodes

global_symbol_table = interpreter.SymbolTable()
global_symbol_table.set("None", interpreter.Number.null)
global_symbol_table.set("False", interpreter.Number.false)
global_symbol_table.set("True", interpreter.Number.true)
global_symbol_table.set("print", interpreter.BuiltInFunction.print)
global_symbol_table.set("input", interpreter.BuiltInFunction.input)
global_symbol_table.set("clear", interpreter.BuiltInFunction.clear)
global_symbol_table.set("is_number", interpreter.BuiltInFunction.is_number)
global_symbol_table.set("is_string", interpreter.BuiltInFunction.is_string)
global_symbol_table.set("is_list", interpreter.BuiltInFunction.is_list)
global_symbol_table.set("is_function", interpreter.BuiltInFunction.is_function)
global_symbol_table.set("append", interpreter.BuiltInFunction.append)
global_symbol_table.set("pop", interpreter.BuiltInFunction.pop)
global_symbol_table.set("extend", interpreter.BuiltInFunction.extend)

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