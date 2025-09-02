import sys
from antlr4 import InputStream, CommonTokenStream
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from EvalVisitor import EvalVisitor

def main(argv):
    if len(argv) > 1:
        with open(argv[1], "r", encoding="utf-8") as f:
            text = f.read()
    else:
        print("Escribe expresiones (Ctrl+D para terminar):")
        text = sys.stdin.read()

    if not text.endswith("\n"):
        text += "\n"

    data = InputStream(text)
    lexer = LabeledExprLexer(data)
    stream = CommonTokenStream(lexer)
    parser = LabeledExprParser(stream)

    prog_ctx = parser.prog()
    visitor = EvalVisitor()

    try:
        stats = prog_ctx.stat()
    except Exception:
        visitor.visit(prog_ctx)
        return

    for st in stats:
        try:
            result = visitor.visit(st)
        except Exception as e:
            print("Error al evaluar sentencia:", e)
            continue
        if result is not None:
            print(result)

if __name__ == "__main__":
    main(sys.argv)
