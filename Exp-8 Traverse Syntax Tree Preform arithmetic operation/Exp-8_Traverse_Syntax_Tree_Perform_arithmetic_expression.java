class TreeNode
{
    String value;
    TreeNode left;
    TreeNode right;

    TreeNode(String value)
    {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}


public class SyntaxTreeTraversal
{
public
    static int traverseAndCalculate(TreeNode node)
    {
        if (node == null)
        {
            return 0;
        }

        if (node.left == null && node.right == null)
        {
            return Integer.parseInt(node.value);
        }
        int leftValue = traverseAndCalculate(node.left);
        int rightValue = traverseAndCalculate(node.right);
        
        switch (node.value)
        {
        case "+":
            return leftValue + rightValue;
        case "-":
            return leftValue - rightValue;
        case "*":
            return leftValue * rightValue;
        case "/":
            if (rightValue == 0)
            {
                throw new ArithmeticException("Division by zero");
            }
            return leftValue / rightValue;
        default:
            throw new IllegalArgumentException("Invalid operator: " + node.value);
        }
    }

public
    static void main(String[] args)
    {
        // Example syntax tree: 3 + (5 * 2)
        TreeNode root = new TreeNode("+");
        root.left = new TreeNode("3");
        root.right = new TreeNode("*");
        root.right.left = new TreeNode("5");
        root.right.right = new TreeNode("2");


        int result = traverseAndCalculate(root);
        System.out.println("Result: " + result);
    }
}
