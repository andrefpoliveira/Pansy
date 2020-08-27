#######################################
# TOKENS
#######################################

T_INT	   		= 'INT'
T_FLOAT    		= 'FLOAT'
T_IDENTIFIER	= 'IDENTIFIER'
T_KEYWORD 		= 'KEYWORD'
T_PLUS     		= 'PLUS'
T_MINUS    		= 'MINUS'
T_MUL      		= 'MUL'
T_DIV      		= 'DIV'
T_INT_DIV		= 'INT_DIV'
T_POW	   		= 'POW'
T_EQ			= 'EQ'
T_LPAREN   		= 'LPAREN'
T_RPAREN   		= 'RPAREN'
T_EE			= 'EE'
T_NE 			= 'NE'
T_GT			= 'GT'
T_LT 			= 'LT'
T_GTE			= 'GTE'
T_LTE			= 'LTE'
T_COMMA			= 'COMMA'
T_ARROW			= 'ARROW'
T_EOF	   		= 'EOF'

class Token:
	def __init__(self, type_, value=None, pos_start=None, pos_end=None):
		self.type = type_
		self.value = value

		if pos_start:
			self.pos_start = pos_start.copy()
			self.pos_end = pos_start.copy()
			self.pos_end.advance()

		if pos_end:
			self.pos_end = pos_end
	
	def __repr__(self):
		if self.value: return f'{self.type}:{self.value}'
		return f'{self.type}'

	def matches(self, type_, value):
		return self.type == type_ and self.value == value