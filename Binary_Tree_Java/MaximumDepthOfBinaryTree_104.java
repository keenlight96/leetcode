

public class MaximumDepthOfBinaryTree_104 {
    public static void main(String[] args) {
        Integer[] arr = {1,null,null};
        TreeNode root = HelperBinaryTree.convertArrayToTreeNode(arr);
        
        MaximumDepthOfBinaryTree_104 solution = new MaximumDepthOfBinaryTree_104();
        int depth = solution.maxDepth(root);
        System.err.println(depth);
    }

    public int maxDepth(TreeNode root) {
        return maxDepthHelper(root, 0);
    }

    public int maxDepthHelper(TreeNode node, int depth) {
        if (node != null) {
            depth++;
            int depthLeft = maxDepthHelper(node.left, depth);
            int depthRight = maxDepthHelper(node.right, depth);
            
            return depthLeft > depthRight ? depthLeft : depthRight;
        } else {
            return depth;
        }
    }
}