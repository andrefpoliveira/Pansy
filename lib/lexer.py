from lib.utils import token, position
from lib import errors
import string

DIGITS      	= '0123456789'
LETTERS			= string.ascii_letters
LETTERS_DIGITS	= LETTERS + DIGITS

KEYWORDS = [
	'var',
	'and',
	'or',
	'not',
	'if',
	'then',
	'elif',
	'else',
	'for',
	'while',
	'step',
	'to',
	'func',
	'end',
	'break',
	'return',
	'continue'
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
			elif self.current_char == '@':
				self.skip_comment()
			elif self.current_char in ';\n':
				tokens.append(token.Token(token.T_NEWLINE, pos_start=self.pos))
				self.advance()
			elif self.current_char in DIGITS:
				tokens.append(self.make_number())
			elif self.current_char in LETTERS:
				tokens.append(self.make_identifier())
			elif self.current_char == '"':
				tokens.append(self.make_string())
			elif self.current_char == '+':
				tokens.append(token.Token(token.T_PLUS, pos_start=self.pos))
				self.advance()
			elif self.current_char == '-':
				tokens.append(self.make_minus_or_arrow())
			elif self.current_char == '*':
				tokens.append(token.Token(token.T_MUL, pos_start=self.pos))
				self.advance()
			elif self.current_char == '/':
				tokens.append(self.make_divisions())
			elif self.current_char == '%':
				tokens.append(token.Token(token.T_REMAINDER, pos_start=self.pos))
				self.advance()
			elif self.current_char == '^':
				tokens.append(token.Token(token.T_POW, pos_start=self.pos))
				self.advance()
			elif self.current_char == '(':
				tokens.append(token.Token(token.T_LPAREN, pos_start=self.pos))
				self.advance()
			elif self.current_char == ')':
				tokens.append(token.Token(token.T_RPAREN, pos_start=self.pos))
				self.advance()
			elif self.current_char == '[':
				tokens.append(token.Token(token.T_LSQUARE, pos_start=self.pos))
				self.advance()
			elif self.current_char == ']':
				tokens.append(token.Token(token.T_RSQUARE, pos_start=self.pos))
				self.advance()
			elif self.current_char == '{':
				tokens.append(token.Token(token.T_LCURLY, pos_start=self.pos))
				self.advance()
			elif self.current_char == '}':
				tokens.append(token.Token(token.T_RCURLY, pos_start=self.pos))
				self.advance()
			elif self.current_char == ':':
				tokens.append(token.Token(token.T_COLON, pos_start=self.pos))
				self.advance()
			elif self.current_char == ',':
				tokens.append(token.Token(token.T_COMMA, pos_start=self.pos))
				self.advance()
			elif self.current_char == '!':
				tok, error = self.make_not_equals()
				if error: return [], error
				tokens.append(tok)
			elif self.current_char == '=':
				tokens.append(self.make_equals())
			elif self.current_char == '<':
				tokens.append(self.make_less_than())
			elif self.current_char == '>':
				tokens.append(self.make_greater_than())
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

	def make_string(self):
		string = ''
		pos_start = self.pos.copy()
		escape_character = False
		self.advance()

		escape_characters = {
			'n': '\n',
			't': '\t'
		}

		while self.current_char != None and (self.current_char != '"' or escape_character):
			if escape_character:
				string += escape_characters.get(self.current_char, self.current_char)
			else:
				if self.current_char == '\\':
					escape_character = True
				else:
					string += self.current_char
			self.advance()
			escape_character = False

		self.advance()
		return token.Token(token.T_STRING, string, pos_start, self.pos)


	def make_not_equals(self):
		pos_start = self.pos.copy()
		self.advance()

		if self.current_char == '=':
			self.advance()
			return token.Token(token.T_NE, pos_start=pos_start, pos_end=self.pos), None

		self.advance()
		return None, errors.ExpectedCharError(pos_start, self.pos,
		"Expected '=' after '!'")

	def make_equals(self):
		tok_type = token.T_EQ
		pos_start = self.pos.copy()
		self.advance()

		if self.current_char == '=':
			self.advance()
			tok_type = token.T_EE

		return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)

	def make_less_than(self):
		tok_type = token.T_LT
		pos_start = self.pos.copy()
		self.advance()

		if self.current_char == '=':
			self.advance()
			tok_type = token.T_LTE

		return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)

	def make_greater_than(self):
		tok_type = token.T_GT
		pos_start = self.pos.copy()
		self.advance()

		if self.current_char == '=':
			self.advance()
			tok_type = token.T_GTE

		return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)

	def make_divisions(self):
		tok_type = token.T_DIV
		pos_start = self.pos.copy()
		self.advance()

		if self.current_char == '/':
			self.advance()
			tok_type = token.T_INT_DIV

		return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)

	def make_minus_or_arrow(self):
		tok_type = token.T_MINUS
		pos_start = self.pos.copy()
		self.advance()

		if self.current_char == '>':
			self.advance()
			tok_type = token.T_ARROW

		return token.Token(tok_type, pos_start=pos_start, pos_end=self.pos)

	def skip_comment(self):
		self.advance()

		while self.current_char != '\n':
			self.advance()

		self.advance()