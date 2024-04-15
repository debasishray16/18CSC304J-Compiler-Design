import java.util.Scanner;
import java.util.Stack;

// Node class to represent each node in the syntax tree
class Node {
    String value;
    Node left, right;

    Node(String item) {
        value = item;
        left = right = null;
    }
}

// Class to perform arithmetic operations
class ArithmeticOperations {
    // Function to traverse the syntax tree and perform arithmetic operations
    static double evaluate(Node root) {
        // Base case: if the node is a leaf node (operand)
        if (root.left == null && root.right == null) {
            return Double.parseDouble(root.value);
        }

        // Evaluate left and right subtrees
        double leftValue = evaluate(root.left);
        double rightValue = evaluate(root.right);

        // Perform arithmetic operation based on the operator
        switch (root.value) {
            case "+":
                return leftValue + rightValue;
            case "-":
                return leftValue - rightValue;
            case "*":
                return leftValue * rightValue;
            case "/":
                if (rightValue == 0) {
                    throw new ArithmeticException("Division by zero!");
                }
                return leftValue / rightValue;
            default:
                throw new IllegalArgumentException("Invalid operator: " + root.value);
        }
    }
}

public class Main {
    // Function to construct syntax tree from infix expression
    static Node constructTree(String expression) {
        Stack<Node> operandStack = new Stack<>();
        Stack<Node> operatorStack = new Stack<>();

        Scanner scanner = new Scanner(expression);
        while (scanner.hasNext()) {
            String token = scanner.next();

            if (isOperator(token)) {
                while (!operatorStack.isEmpty() && precedence(operatorStack.peek().value) >= precedence(token)) {
                    processOperator(operandStack, operatorStack);
                }
                operatorStack.push(new Node(token));
            } else if (token.equals("(")) {
                operatorStack.push(new Node(token));
            } else if (token.equals(")")) {
                while (!operatorStack.peek().value.equals("(")) {
                    processOperator(operandStack, operatorStack);
                }
                operatorStack.pop(); // Discard "("
            } else {
                operandStack.push(new Node(token));
            }
        }

        while (!operatorStack.isEmpty()) {
            processOperator(operandStack, operatorStack);
        }

        return operandStack.pop();
    }

    static void processOperator(Stack<Node> operandStack, Stack<Node> operatorStack) {
        Node operatorNode = operatorStack.pop();
        Node rightOperand = operandStack.pop();
        Node leftOperand = operandStack.pop();

        operatorNode.left = leftOperand;
        operatorNode.right = rightOperand;
        operandStack.push(operatorNode);
    }

    static int precedence(String operator) {
        switch (operator) {
            case "+":
            case "-":
                return 1;
            case "*":
            case "/":
                return 2;
            default:
                return 0; // Assuming "(" has lowest precedence
        }
    }

    static boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the infix expression: ");
        String expression = scanner.nextLine();

        // Construct syntax tree
        Node root = constructTree(expression);

        // Evaluate the syntax tree and print the result
        double result = ArithmeticOperations.evaluate(root);
        System.out.println("Result: " + result);
    }
}
