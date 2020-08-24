from lib.utils import token, position
from lib import errors
import string

DIGITS      	= '0123456789'
LETTERS			= string.ascii_letters
LETTERS_DIGITS	= LETTERS + DIGITS

KEYWORDS = [
	'var'
]

#######################################
# LEXER
#######################################

class Lexer:
	def __init__(self, fn, text):
		self.fn = fn
		self.text = text
		self.pos = position.Position(-1, 0, -1, fn, text)
		self.current_char = None
		self.advance()
	
	def advance(self):
		self.pos.advance(self.current_char)
		self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

	def make_tokens(self):
		tokens = []

		while self.current_char != None:
			if self.current_char in ' \t':
				self.advance()
			elif self.current_char in DIGITS:
				tokens.append(self.make_number())
			elif self.current_char in LETTERS:
				tokens.append(self.make_identifier())
			elif self.current_char == '+':
				tokens.append(token.Token(token.T_PLUS, pos_start=self.pos))
				self.advance()
			elif self.current_char == '-':
				tokens.append(token.Token(token.T_MINUS, pos_start=self.pos))
				self.advance()
			elif self.current_char == '*':
				tokens.append(token.Token(token.T_MUL, pos_start=self.pos))
				self.advance()
			elif self.current_char == '/':
				tokens.append(token.Token(token.T_DIV, pos_start=self.pos))
				self.advance()
			elif self.current_char == '^':
				tokens.append(token.Token(token.T_POW, pos_start=self.pos))
				self.advance()
			elif self.current_char == '=':
				tokens.append(token.Token(token.T_EQ, pos_start=self.pos))
				self.advance()
			elif self.current_char == '(':
				tokens.append(token.Token(token.T_LPAREN, pos_start=self.pos))
				self.advance()
			elif self.current_char == ')':
				tokens.append(token.Token(token.T_RPAREN, pos_start=self.pos))
				self.advance()
			else:
				pos_start = self.pos.copy()
				char = self.current_char
				self.advance()
				return [], errors.IllegalCharError(pos_start, self.pos, "'" + char + "'")

		tokens.append(token.Token(token.T_EOF, pos_start=self.pos))
		return tokens, None

	def make_number(self):
		num_str = ''
		dot_count = 0
		pos_start = self.pos.copy()

		while self.current_char != None and self.current_char in DIGITS + '.':
			if self.current_char == '.':
				if dot_count == 1: break
				dot_count += 1
				num_str += '.'
			else:
				num_str += self.current_char
			self.advance()

		if dot_count == 0:
			return token.Token(token.T_INT, int(num_str), pos_start, self.pos)
		else:
			return token.Token(token.T_FLOAT, float(num_str), pos_start, self.pos)

	def make_identifier(self):
		id_str = ''
		pos_start = self.pos.copy()

		while self.current_char != None and self.current_char in LETTERS_DIGITS + '_':
			id_str += self.current_char
			self.advance()

		tok_type = token.T_KEYWORD if id_str in KEYWORDS else token.T_IDENTIFIER
		return token.Token(tok_type, id_str, pos_start, self.pos)