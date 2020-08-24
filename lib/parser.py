from lib.utils import token, nodes
from lib import errors

#######################################
# PARSE RESULT
#######################################

class ParseResult:
	def __init__(self):
		self.error = None
		self.node = None

	def register(self, res):
		if isinstance(res, ParseResult):
			if res.error: self.error = res.error
			return res.node

		return res

	def success(self, node):
		self.node = node
		return self

	def failure(self, error):
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
			res.register(self.advance())
			return res.success(nodes.NumberNode(tok))

		elif tok.type == token.T_LPAREN:
			res.register(self.advance())
			expr = res.register(self.expr())
			if res.error: return res
			if self.current_tok.type == token.T_RPAREN:
				res.register(self.advance())
				return res.success(expr)
			else:
				return res.failure(errors.InvalidSyntaxError(
					self.current_tok.pos_start, self.current_tok.pos_end,
					"Expected ')'"
				))

		return res.failure(errors.InvalidSyntaxError(
			tok.pos_start, tok.pos_end,
			"Expected int or float, '+', '-' or '('"
		))

	def power(self):
		return self.bin_op(self.atom, (token.T_POW), self.factor)


	def factor(self):
		res = ParseResult()
		tok = self.current_tok

		if tok.type in (token.T_PLUS, token.T_MINUS):
			res.register(self.advance())
			factor = res.register(self.factor())
			if res.error: return res
			return res.success(nodes.UnaryOpNode(tok, factor))

		return self.power()

	def term(self):
		return self.bin_op(self.factor, (token.T_MUL, token.T_DIV))

	def expr(self):
		return self.bin_op(self.term, (token.T_PLUS, token.T_MINUS))

	###################################

	def bin_op(self, func_a, ops, func_b=None):
		if func_b == None:
			func_b = func_a
		
		res = ParseResult()
		left = res.register(func_a())
		if res.error: return res

		while self.current_tok.type in ops:
			op_tok = self.current_tok
			res.register(self.advance())
			right = res.register(func_b())
			if res.error: return res
			left = nodes.BinOpNode(left, op_tok, right)

		return res.success(left)