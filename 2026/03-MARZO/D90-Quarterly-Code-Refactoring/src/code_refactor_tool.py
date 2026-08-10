import ast
from typing import List

class CodeRefactorAnalyzer(ast.NodeVisitor):
    def __init__(self, max_lines: int = 10):
        self.max_lines = max_lines
        self.long_functions: List[str] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        """Analiza la longitud de las funciones utilizando el AST."""
        if node.body:
            start_line = node.lineno
            end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line
            duration = end_line - start_line + 1
            
            if duration > self.max_lines:
                self.long_functions.append(node.name)
                
        self.generic_visit(node)

    def analyze_source_code(self, source_code: str) -> List[str]:
        """Procesa el código fuente y devuelve una lista con los nombres de las funciones demasiado largas."""
        self.long_functions = []
        tree = ast.parse(source_code)
        self.visit(tree)
        return self.long_functions