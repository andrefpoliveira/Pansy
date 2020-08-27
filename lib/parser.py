from lib.utils import token, nodes
from lib import errors

#######################################
# PARSE RESULT
#######################################

class ParseResult:
	def __init__(self):
		self.error = None
		self.node = None
		self.advanced_count = 0

	def register_advancement(self):
		self.advanced_count += 1

	def register(self, res):
		self.advanced_count += res.advanced_count
		if res.error: self.error = res.error
		return res.node

	def success(self, node):
		self.node = node
		return self

	def failure(self, error):
		if not self.error or self.advanced_count == 0:
			self.error = error
		return self

#######################################
# PARSER
#######################################

class Parser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.tok_idx = -1
		self.advance()

	def advance(self, ):
		self.tok_idx += 1
		if self.tok_idx < len(self.tokens):
			self.current_tok = self.tokens[self.tok_idx]
		return self.current_tok

	def parse(self):
		res = self.expr()
		if not res.error and self.current_tok.type != token.T_EOF:
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				"Expected '+', '-', '*' or '/'"
			))
		return res

	###################################

	def atom(self):
		res = ParseResult()
		tok = self.current_tok

		if tok.type in (token.T_INT, token.T_FLOAT):
			res.register_advancement()
			self.advance()
			return res.success(nodes.NumberNode(tok))

		elif tok.type == token.T_IDENTIFIER:
			res.register_advancement()
			self.advance()
			return res.success(nodes.VarAccessNode(tok))

		elif tok.type == token.T_LPAREN:
			res.register_advancement()
			self.advance()
			expr = res.register(self.expr())
			if res.error: return res
			if self.current_tok.type == token.T_RPAREN:
				res.register_advancement()
				self.advance()
				return res.success(expr)
			else:
				return res.failure(errors.InvalidSyntaxError(
					self.current_tok.pos_start, self.current_tok.pos_end,
					"Expected ')'"
				))
		elif tok.matches(token.T_KEYWORD, 'if'):
			if_expr = res.register(self.if_expr())
			if res.error: return res
			return res.success(if_expr)

		elif tok.matches(token.T_KEYWORD, 'for'):
			for_expr = res.register(self.for_expr())
			if res.error: return res
			return res.success(for_expr)

		elif tok.matches(token.T_KEYWORD, 'while'):
			while_expr = res.register(self.while_expr())
			if res.error: return res
			return res.success(while_expr)

		return res.failure(errors.InvalidSyntaxError(
			tok.pos_start, tok.pos_end,
			"Expected int or float, identifier, '+', '-' or '('"
		))

	def power(self):
		return self.bin_op(self.atom, (token.T_POW, ), self.factor)


	def factor(self):
		res = ParseResult()
		tok = self.current_tok

		if tok.type in (token.T_PLUS, token.T_MINUS):
			res.register_advancement()
			self.advance()
			factor = res.register(self.factor())
			if res.error: return res
			return res.success(nodes.UnaryOpNode(tok, factor))

		return self.power()

	def term(self):
		return self.bin_op(self.factor, (token.T_MUL, token.T_DIV, token.T_INT_DIV))

	def arithm_expr(self):
		return self.bin_op(self.term, (token.T_PLUS, token.T_MINUS))

	def comp_expr(self):
		res = ParseResult()

		if self.current_tok.matches(token.T_KEYWORD, 'not'):
			op_tok = self.current_tok
			res.register_advancement()
			self.advance()

			node = res.register(self.comp_expr())
			if res.error: return res
			return res.success(nodes.UnaryOpNode(op_tok, node))

		node = res.register(self.bin_op(self.arithm_expr, (token.T_EE, token.T_NE, token.T_LT, token.T_GT, token.T_LTE, token.T_GTE)))

		if res.error:
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				"Expected int or float, identifier, '+', '-', '(' or 'not'"
			))

		return res.success(node)

	def expr(self):
		res = ParseResult()

		if self.current_tok.matches(token.T_KEYWORD, 'var'):
			res.register_advancement()
			self.advance()
		
			if self.current_tok.type != token.T_IDENTIFIER:
				return res.failure(errors.InvalidSyntaxError(
					self.current_tok.pos_start, self.current_tok.pos_end,
					"Expected identifier"
				))

			var_name = self.current_tok
			res.register_advancement()
			self.advance()

			if self.current_tok.type != token.T_EQ:
				return res.failure(errors.InvalidSyntaxError(
					self.current_tok.pos_start, self.current_tok.pos_end,
					"Expected '='"
				))

			res.register_advancement()
			self.advance()
			expr = res.register(self.expr())

			if res.error: return res
			return res.success(nodes.VarAssignNode(var_name, expr))

		node = res.register(self.bin_op(self.comp_expr, ((token.T_KEYWORD, 'and'), (token.T_KEYWORD, 'or'))))

		if res.error:
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				"Expected int or float, identifier, 'var', '+', '-' or '('"
			))

		return res.success(node)

	def if_expr(self):
		res = ParseResult()
		cases = []
		else_case = None

		if not self.current_tok.matches(token.T_KEYWORD, 'if'):
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected 'if"
			))

		res.register_advancement()
		self.advance()

		condition = res.register(self.expr())
		if res.error: return res

		if not self.current_tok.matches(token.T_KEYWORD, 'then'):
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected 'then"
			))

		res.register_advancement()
		self.advance()

		expr = res.register(self.expr())
		if res.error: return res
		cases.append((condition, expr))

		while self.current_tok.matches(token.T_KEYWORD, 'elif'):
			res.register_advancement()
			self.advance()

			condition = res.register(self.expr())
			if res.error: return res

			if not self.current_tok.matches(token.T_KEYWORD, 'then'):
				if not self.current_tok.matches(token.T_KEYWORD, 'then'):
					return res.failure(errors.InvalidSyntaxError(
						self.current_tok.pos_start, self.current_tok.pos_end,
						f"Expected 'then"
					))

			res.register_advancement()
			self.advance()

			expr = res.register(self.expr())
			if res.error: return res
			cases.append((condition, expr))

		if self.current_tok.matches(token.T_KEYWORD, 'else'):
			res.register_advancement()
			self.advance()

			expr = res.register(self.expr())
			if res.error: return res
			else_case = expr

		return res.success(nodes.IfNode(cases, else_case))

	def for_expr(self):
		res = ParseResult()

		if not self.current_tok.matches(token.T_KEYWORD, 'for'):
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected 'for'"
			))

		res.register_advancement()
		self.advance()

		if self.current_tok.type != token.T_IDENTIFIER:
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected identifier"
			))

		var_name = self.current_tok
		res.register_advancement()
		self.advance()

		if self.current_tok.type != token.T_EQ:
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected '='"
			))
		
		res.register_advancement()
		self.advance()

		start_value = res.register(self.expr())
		if res.error: return res

		if not self.current_tok.matches(token.T_KEYWORD, 'to'):
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected 'to'"
			))
		
		res.register_advancement()
		self.advance()

		end_value = res.register(self.expr())
		if res.error: return res

		if self.current_tok.matches(token.T_KEYWORD, 'step'):
			res.register_advancement()
			self.advance()

			step_value = res.register(self.expr())
			if res.error: return res
		else:
			step_value = None

		if not self.current_tok.matches(token.T_KEYWORD, 'then'):
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected 'then'"
			))

		res.register_advancement()
		self.advance()

		body = res.register(self.expr())
		if res.error: return res

		return res.success(nodes.ForNode(var_name, start_value, end_value, step_value, body))

	def while_expr(self):
		res = ParseResult()

		if not self.current_tok.matches(token.T_KEYWORD, 'while'):
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected 'while'"
			))

		res.register_advancement()
		self.advance()

		condition = res.register(self.expr())
		if res.error: return res

		if not self.current_tok.matches(token.T_KEYWORD, 'then'):
			return res.failure(errors.InvalidSyntaxError(
				self.current_tok.pos_start, self.current_tok.pos_end,
				f"Expected 'then'"
			))

		res.register_advancement()
		self.advance()

		body = res.register(self.expr())
		if res.error: return res

		return res.success(nodes.WhileNode(condition, body))

	###################################

	def bin_op(self, func_a, ops, func_b=None):
		if func_b == None:
			func_b = func_a
		
		res = ParseResult()
		left = res.register(func_a())
		if res.error: return res

		while self.current_tok.type in ops or (self.current_tok.type, self.current_tok.value) in ops:
			op_tok = self.current_tok
			res.register_advancement()
			self.advance()
			right = res.register(func_b())
			if res.error: return res
			left = nodes.BinOpNode(left, op_tok, right)

		return res.success(left)