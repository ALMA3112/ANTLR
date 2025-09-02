import java.util.*;

// Evalúa expresiones matemáticas con decimales
public class EvalVisitor extends LabeledExprBaseVisitor<Double> {

    Map<String, Double> memoria = new HashMap<>();

    @Override
    public Double visitAsignar(LabeledExprParser.AsignarContext ctx) {
        String nombre = ctx.ID().getText();
        double valor = visit(ctx.expr());
        memoria.put(nombre, valor);
        return valor;
    }

    // Imprimir resultado 
    @Override
    public Double visitImprimirExpr(LabeledExprParser.ImprimirExprContext ctx) {
        Double valor = visit(ctx.expr());
        System.out.println(String.format("%.2f", valor));
        return 0.0;
    }

    // Leer número entero
    @Override
    public Double visitEntero(LabeledExprParser.EnteroContext ctx) {
        return Double.valueOf(ctx.NUM().getText());
    }

    // Leer variable
    @Override
    public Double visitIdentificador(LabeledExprParser.IdentificadorContext ctx) {
        String nombre = ctx.ID().getText();
        return memoria.getOrDefault(nombre, 0.0);
    }

    // Multiplicación y división
    @Override
    public Double visitMultiplicarDividir(LabeledExprParser.MultiplicarDividirContext ctx) {
        double izquierda = visit(ctx.expr(0));
        double derecha = visit(ctx.expr(1));
        return ctx.op.getType() == LabeledExprParser.MUL ? izquierda * derecha : izquierda / derecha;
    }

    // Suma y resta
    @Override
    public Double visitSumarRestar(LabeledExprParser.SumarRestarContext ctx) {
        double izquierda = visit(ctx.expr(0));
        double derecha = visit(ctx.expr(1));
        return ctx.op.getType() == LabeledExprParser.ADD ? izquierda + derecha : izquierda - derecha;
    }

    // Paréntesis
    @Override
    public Double visitParentesis(LabeledExprParser.ParentesisContext ctx) {
        return visit(ctx.expr());
    }

    // Llamada a funciones matemáticas
    @Override
    public Double visitLlamadaFuncion(LabeledExprParser.LlamadaFuncionContext ctx) {
        String funcion = ctx.funcion().getText();
        double x = visit(ctx.expr());

        switch (funcion) {
            case "sin": return Math.sin(Math.toRadians(x));
            case "cos": return Math.cos(Math.toRadians(x));
            case "tan": return Math.tan(Math.toRadians(x));
            case "sqrt": return Math.sqrt(x);
            case "ln": return Math.log(x);
            case "log": return Math.log10(x);
            case "rad": return Math.toRadians(x);
            case "deg": return Math.toDegrees(x);
            default: return 0.0;
        }
    }

    // Factorial (solo válido para enteros)
    @Override
    public Double visitFactorial(LabeledExprParser.FactorialContext ctx) {
        int n = (int)Math.round(visit(ctx.expr()));
        double resultado = 1;
        for (int i = 2; i <= n; i++) resultado *= i;
        return resultado;
    }
}
