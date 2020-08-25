from lib.utils import token
from lib import errors

#######################################
# RUNTIME RESULT
#######################################

class RTResult:
	def __init__(self):
		self.value = None
		self.error = None

	def register(self, res):
		if res.error: self.error = res.error
		return res.value

	def success(self, value):
		self.value = value
		return self

	def failure(self, error):
		self.error = error
		return self

#######################################
# VALUES
#######################################

class Number:
	def __init__(self, value):
		self.value = value
		self.set_pos()
		self.set_context()

	def set_pos(self, pos_start=None, pos_end=None):
		self.pos_start = pos_start
		self.pos_end = pos_end
		return self

	def set_context(self, context=None):
		self.context = context
		return self

	def added_to(self, other):
		if isinstance(other, Number):
			return Number(self.value + other.value).set_context(self.context), None

	def subbed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value - other.value).set_context(self.context), None

	def multed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value * other.value).set_context(self.context), None

	def dived_by(self, other):
		if isinstance(other, Number):
			if other.value == 0:
				return None, errors.RTError(
					other.pos_start, other.pos_end,
					'Division by zero',
					self.context
				)

			return Number(self.value / other.value).set_context(self.context), None

	def int_dived_by(self, other):
		if isinstance(other, Number):
			if other.value == 0:
				return None, errors.RTError(
					other.pos_start, other.pos_end,
					'Division by zero',
					self.context
				)

			return Number(self.value // other.value).set_context(self.context), None

	def powed_by(self, other):
		if isinstance(other, Number):
			return Number(self.value ** other.value).set_context(self.context), None

	def get_comp_ee(self, other):
		if isinstance(other, Number):
			return Number(int(self.value == other.value)).set_context(self.context), None

	def get_comp_ne(self, other):
		if isinstance(other, Number):
			return Number(int(self.value != other.value)).set_context(self.context), None

	def get_comp_lt(self, other):
		if isinstance(other, Number):
			return Number(int(self.value < other.value)).set_context(self.context), None

	def get_comp_gt(self, other):
		if isinstance(other, Number):
			return Number(int(self.value > other.value)).set_context(self.context), None

	def get_comp_lte(self, other):
		if isinstance(other, Number):
			return Number(int(self.value <= other.value)).set_context(self.context), None

	def get_comp_gte(self, other):
		if isinstance(other, Number):
			return Number(int(self.value >= other.value)).set_context(self.context), None

	def and_with(self, other):
		if isinstance(other, Number):
			return Number(int(self.value and other.value)).set_context(self.context), None

	def or_with(self, other):
		if isinstance(other, Number):
			return Number(int(self.value or other.value)).set_context(self.context), None

	def notted(self):
		return Number(1 if self.value == 0 else 0).set_context(self.context), None

	def copy(self):
		copy = Number(self.value)
		copy.set_pos(self.pos_start, self.pos_end)
		copy.set_context(self.context)
		return copy

	def __repr__(self):
		return str(self.value)

#######################################
# CONTEXT
#######################################

class Context:
	def __init__(self, display_name, parent=None, parent_entry_pos=None):
		self.display_name = display_name
		self.parent = parent
		self.parent_entry_pos = parent_entry_pos
		self.symbol_table = None

#######################################
# SYMBOL TABLE
#######################################

class SymbolTable:
	def __init__(self):
		self.symbols = {}
		self.parent = None

	def get(self, name):
		value = self.symbols.get(name, None)
		if value == None and self.parent:
			return self.parent.get(name)
		return value

	def set(self, name, value):
		self.symbols[name] = value

	def remove(self, name):
		del self.symbols[name]

#######################################
# INTERPRETER
#######################################

class Interpreter:
	def visit(self, node, context):
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name, self.no_visit_method)
		return method(node, context)

	def no_visit_method(self, node, context):
		raise Exception(f'No visit_{type(node).__name__} method defined')

	###################################

	def visit_NumberNode(self, node, context):
		return RTResult().success(
			Number(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
		)

	def visit_VarAccessNode(self, node, context):
		res = RTResult()
		var_name = node.var_name_tok.value
		value = context.symbol_table.get(var_name)

		if not value:
			return res.failure(errors.RTError(
				node.pos_start, node.pos_end,
				f"'{var_name}' is not defined",
				context
			))
		value = value.copy().set_pos(node.pos_start, node.pos_end)
		return res.success(value)

	def visit_VarAssignNode(self, node, context):
		res = RTResult()
		var_name = node.var_name_tok.value
		value = res.register(self.visit(node.value_node, context))

		if res.error: return res

		context.symbol_table.set(var_name, value)
		return res.success(value)

	def visit_BinOpNode(self, node, context):
		res = RTResult()
		left = res.register(self.visit(node.left_node, context))
		if res.error: return res
		right = res.register(self.visit(node.right_node, context))
		if res.error: return res

		if node.op_tok.type == token.T_PLUS:
			result, error = left.added_to(right)
		elif node.op_tok.type == token.T_MINUS:
			result, error = left.subbed_by(right)
		elif node.op_tok.type == token.T_MUL:
			result, error = left.multed_by(right)
		elif node.op_tok.type == token.T_DIV:
			result, error = left.dived_by(right)
		elif node.op_tok.type == token.T_INT_DIV:
			result, error = left.int_dived_by(right)
		elif node.op_tok.type == token.T_POW:
			result, error = left.powed_by(right)
		elif node.op_tok.type == token.T_EE:
			result, error = left.get_comp_ee(right)
		elif node.op_tok.type == token.T_NE:
			result, error = left.get_comp_ne(right)
		elif node.op_tok.type == token.T_LT:
			result, error = left.get_comp_lt(right)
		elif node.op_tok.type == token.T_GT:
			result, error = left.get_comp_gt(right)
		elif node.op_tok.type == token.T_LTE:
			result, error = left.get_comp_lte(right)
		elif node.op_tok.type == token.T_GTE:
			result, error = left.get_comp_gte(right)
		elif node.op_tok.matches(token.T_KEYWORD, 'and'):
			result, error = left.and_with(right)
		elif node.op_tok.matches(token.T_KEYWORD, 'or'):
			result, error = left.or_with(right)

		if error:
			return res.failure(error)
		else:
			return res.success(result.set_pos(node.pos_start, node.pos_end))

	def visit_UnaryOpNode(self, node, context):
		res = RTResult()
		number = res.register(self.visit(node.node, context))
		if res.error: return res

		error = None

		if node.op_tok.type == token.T_MINUS:
			number, error = number.multed_by(Number(-1))
		if node.op_tok.matches(token.T_KEYWORD, 'not'):
			number, error = number.notted()

		if error:
			return res.failure(error)
		else:
			return res.success(number.set_pos(node.pos_start, node.pos_end))