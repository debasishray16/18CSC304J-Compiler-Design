import java.util.*;

public class Main {

    public static void main(String[] args) {
        IntermediateCodeGenerator generator = new IntermediateCodeGenerator();
        
        // Example usage for If statement
        String ifCondition = "x > 5";
        String trueLabel = "L1";
        String falseLabel = "L2";
        System.out.println(generator.generateIfCode(ifCondition, trueLabel, falseLabel));

        // Example usage for While statement
        String whileCondition = "x < 10";
        String startLabel = "LoopStart";
        String endLabel = "LoopEnd";
        System.out.println(generator.generateWhileStartCode(whileCondition, startLabel));
        System.out.println(generator.generateWhileEndCode(endLabel, startLabel));

        // Additional constraints
        String constraintLabel3 = "L3";
        String constraintLabel4 = "L4";
        System.out.println(generator.generateIfCode("y == 0", constraintLabel3, constraintLabel4));
        System.out.println(generator.generateWhileStartCode("y != 0", "LoopStart2"));
        System.out.println(generator.generateWhileEndCode("LoopEnd2", "LoopStart2"));
    }
}

class IntermediateCodeGenerator {
    
    private int labelCount = 0;
    
    public String generateIfCode(String condition, String trueLabel, String falseLabel) {
        return "if (" + condition + ") goto " + trueLabel + "; else goto " + falseLabel + ";";
    }
    
    public String generateWhileStartCode(String condition, String startLabel) {
        return startLabel + ": if (" + condition + ") goto ";
    }
    
    public String generateWhileEndCode(String endLabel, String startLabel) {
        return "goto " + startLabel + "; " + endLabel + ":";
    }
}