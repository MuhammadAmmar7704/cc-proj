from typing import List
from .lexer import Lexer, Token
from . import ast as A

class ParseError(Exception):
    pass

class Parser:
    """Recursive descent parser that builds an Abstract Syntax Tree"""
    
    def __init__(self, code: str):
        self.tokens = Lexer(code).tokenize()
        self.pos = 0

    def peek(self) -> Token:
        """Look at current token without consuming it"""
        return self.tokens[self.pos]

    def next(self) -> Token:
        """Consume and return current token"""
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def accept(self, val: str) -> bool:
        """Try to match a token, consume if matches"""
        if self.peek().value == val or self.peek().type == val:
            self.next();
            return True
        return False

    def expect(self, val: str) -> Token:
        """Match a token or raise error"""
        if not (self.peek().value == val or self.peek().type == val):
            t = self.peek()
            raise ParseError(f'Expected {val} got {t.type} {t.value} at {t.line}:{t.column}')
        return self.next()

    def parse(self) -> A.Program:
        """Main entry point - parse entire program"""
        body: List[A.Stmt] = []
        while self.peek().type != 'EOF':
            while self.accept('NEWLINE'):
                pass
            if self.peek().type == 'EOF':
                break
            body.append(self.statement())
            while self.accept('NEWLINE'):
                pass
        return A.Program(body)

    def statement(self) -> A.Stmt:
        """Parse a single statement (let, seq, print, loop, or if)"""
        tok = self.peek()
        
        # Integer variable declaration: let x = expr
        if tok.type == 'let':
            self.next()
            name = self.expect('IDENT').value
            self.expect('=')
            val = self.expr()
            return A.Let(name, val)
            
        # Sequence variable declaration: seq s = fibonacci(n)
        if tok.type == 'seq':
            self.next()
            name = self.expect('IDENT').value
            self.expect('=')
            val = self.seq_expr()
            return A.SeqDecl(name, val)
            
        # Print statement: print expr
        if tok.type == 'print':
            self.next()
            val = self.expr()
            return A.Print(val)
            
        # Loop: loop i from 0 to 10 { ... }
        if tok.type == 'loop':
            self.next()
            var = self.expect('IDENT').value
            self.expect('from')
            start = self.expr()
            self.expect('to')
            end = self.expr()
            body = self.compound()
            return A.Loop(var, start, end, body)
            
        # Conditional: if expr { ... } else { ... }
        if tok.type == 'if':
            self.next()
            cond = self.expr()
            then_body = self.compound()
            else_body = None
            if self.accept('else'):
                else_body = self.compound()
            return A.If(cond, then_body, else_body)
            
        raise ParseError(f'Unknown statement at {tok.line}:{tok.column}')

    def compound(self) -> List[A.Stmt]:
        """Parse a block of statements enclosed in braces { ... }"""
        self.expect('{')
        body: List[A.Stmt] = []
        while not self.accept('}'):
            while self.accept('NEWLINE'):
                pass
            body.append(self.statement())
            while self.accept('NEWLINE'):
                pass
        return body

    def seq_expr(self) -> A.Expr:
        """Parse sequence expressions: fibonacci(n) or range(start, end)"""
        if self.accept('fibonacci'):
            self.expect('(')
            n = self.expr()
            self.expect(')')
            return A.SeqFibonacci(n)
        if self.accept('range'):
            self.expect('(')
            s = self.expr()
            self.expect(',')
            e = self.expr()
            self.expect(')')
            return A.SeqRange(s, e)
        raise ParseError('Expected sequence expression')

    def expr(self) -> A.Expr:
        """Entry point for expression parsing"""
        return self.logic()

    def logic(self) -> A.Expr:
        """Parse logical operators: && and ||"""
        left = self.equality()
        while self.peek().type in ('&&', '||'):
            op = self.next().type
            right = self.equality()
            left = A.Binary(op, left, right)
        return left

    def equality(self) -> A.Expr:
        left = self.rel()
        while self.peek().type in ('==', '!='):
            op = self.next().type
            right = self.rel()
            left = A.Binary(op, left, right)
        return left

    def rel(self) -> A.Expr:
        left = self.add()
        while self.peek().type in ('<', '<=', '>', '>='):
            op = self.next().type
            right = self.add()
            left = A.Binary(op, left, right)
        return left

    def add(self) -> A.Expr:
        left = self.mul()
        while self.peek().type in ('+', '-'):
            op = self.next().type
            right = self.mul()
            left = A.Binary(op, left, right)
        return left

    def mul(self) -> A.Expr:
        left = self.unary()
        while self.peek().type in ('*', '/', '%'):
            op = self.next().type
            right = self.unary()
            left = A.Binary(op, left, right)
        return left

    def unary(self) -> A.Expr:
        if self.accept('-'):
            return A.Unary('-', self.unary())
        return self.primary()

    def primary(self) -> A.Expr:
        tok = self.peek()
        if tok.type == 'NUMBER':
            self.next()
            return A.Number(int(tok.value))
        if tok.type == 'IDENT':
            self.next()
            return A.Var(tok.value)
        if self.accept('('):
            e = self.expr()
            self.expect(')')
            return e
        if tok.type in ('true','false'):
            self.next()
            return A.Number(1 if tok.type == 'true' else 0)
        raise ParseError(f'Unexpected token {tok.type} {tok.value} at {tok.line}:{tok.column}')
