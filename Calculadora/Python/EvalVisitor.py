from LabeledExprVisitor import LabeledExprVisitor
from LabeledExprParser import LabeledExprParser
import math

class EvalVisitor(LabeledExprVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}

    def visitProg(self, ctx):
        return None

    def visitStat(self, ctx):
        return self.visitChildren(ctx)

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return None  

    def visitPrintExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitBlank(self, ctx):
        return None

    def visitInt(self, ctx):
        return float(ctx.INT().getText())

    def visitId(self, ctx):
        name = ctx.ID().getText()
        return float(self.memory.get(name, 0.0))

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.MUL:
            return left * right
        else:
            if right == 0:
                raise ZeroDivisionError("División por cero")
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.ADD:
            return left + right
        else:
            return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitFuncCall(self, ctx):
        name = ctx.ID().getText()
        args = [self.visit(e) for e in ctx.expr()]
        if name == "sin":
            return math.sin(args[0])
        if name == "cos":
            return math.cos(args[0])
        if name == "tan":
            return math.tan(args[0])
        if name == "sqrt":
            return math.sqrt(args[0])
        if name == "ln":
            return math.log(args[0])
        if name == "log":
            return math.log10(args[0])
        if name in ("pow", "powf"):
            if len(args) != 2:
                raise Exception("pow requiere 2 argumentos")
            return math.pow(args[0], args[1])
        if name == "max":
            return max(args)
        if name == "min":
            return min(args)
        raise Exception(f"Función desconocida: {name}")
