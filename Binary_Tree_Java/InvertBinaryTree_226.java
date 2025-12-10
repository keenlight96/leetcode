
import java.util.ArrayList;

public class InvertBinaryTree_226 {
    public static void main(String[] args) {
        Integer[] arr = {};
        TreeNode root = HelperBinaryTree.convertArrayToTreeNode(arr);
        
        InvertBinaryTree_226 solution = new InvertBinaryTree_226();
        root = solution.invertTree(root);

        ArrayList arr2 = HelperBinaryTree.convertTreeNodeToArray(root);
        System.err.println(arr2);
    }

    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        root.left = invertTree(root.left);
        root.right = invertTree(root.right);

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        return root;
    }
}

