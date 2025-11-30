from dataclasses import dataclass
from typing import List

@dataclass
class Token:
    """Represents a single token with its type, value, and position"""
    type: str
    value: str
    line: int
    column: int

# Reserved words that cannot be used as variable names
KEYWORDS = {
    'let', 'seq', 'print', 'loop', 'from', 'to', 'if', 'else', 'true', 'false',
    'fibonacci', 'range'
}

# Punctuation symbols
SYMBOLS = {
    '{', '}', '(', ')', ',',
}

# Operators (two-character operators must be checked before single-character)
OPERATORS = {
    '==', '!=', '<=', '>=', '&&', '||',
    '+', '-', '*', '/', '%', '<', '>', '='
}

class Lexer:
    """Converts source code into a stream of tokens"""
    
    def __init__(self, code: str):
        self.code = code

    def tokenize(self) -> List[Token]:
        """Main tokenization loop - scans characters and produces tokens"""
        tokens: List[Token] = []
        i = 0
        line = 1
        col = 1
        src = self.code

        def emit(t, v):
            """Helper to add a token to the list"""
            tokens.append(Token(t, v, line, col))

        while i < len(src):
            ch = src[i]
            
            # Skip whitespace
            if ch in ' \t':
                i += 1; col += 1
                continue
                
            # Handle newlines
            if ch == '\n':
                emit('NEWLINE', '\n')
                i += 1; line += 1; col = 1
                continue
                
            # Skip comments (from # to end of line)
            if ch == '#':
                while i < len(src) and src[i] != '\n':
                    i += 1; col += 1
                continue
                
            # Recognize numbers
            if ch.isdigit():
                start = i
                while i < len(src) and src[i].isdigit():
                    i += 1
                emit('NUMBER', src[start:i])
                col += (i - start)
                continue
                
            # Recognize identifiers and keywords
            if ch.isalpha() or ch == '_':
                start = i
                while i < len(src) and (src[i].isalnum() or src[i] == '_'):
                    i += 1
                word = src[start:i]
                # Check if it's a keyword, otherwise it's an identifier
                typ = word if word in KEYWORDS else 'IDENT'
                emit(typ, word)
                col += (i - start)
                continue
                
            # Check for two-character operators first
            two = src[i:i+2]
            if two in OPERATORS:
                emit(two, two)
                i += 2; col += 2
                continue
                
            # Then check single-character operators
            if ch in OPERATORS:
                emit(ch, ch)
                i += 1; col += 1
                continue
                
            # Check symbols
            if ch in SYMBOLS:
                emit(ch, ch)
                i += 1; col += 1
                continue
                
            # If we get here, it's an invalid character
            raise SyntaxError(f'Unknown character {ch} at {line}:{col}')
            
        tokens.append(Token('EOF', '', line, col))
        return tokens
