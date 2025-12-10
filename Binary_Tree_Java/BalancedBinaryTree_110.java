
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BalancedBinaryTree_110 {
    Integer depth1 = null;
    Integer depth2 = null;
    Integer countDepth1 = 0;
    ArrayList<Integer> depths = new ArrayList<>();

    public static void main(String[] args) {
        Integer[] arr1 = {1,2,2,3,3,null,null,4,4};
        List<Integer> arr = new ArrayList<>(Arrays.asList(arr1));
        TreeNode root = HelperBinaryTree.arrayToBinaryTree(arr);
        
        BalancedBinaryTree_110 solution = new BalancedBinaryTree_110();
        boolean result = solution.isBalanced(root);

        System.err.println(result);
    }

    public boolean isBalanced(TreeNode root) {
        boolean res = maxDepthHelper(root, 0);
        return res && (depths.size() == 1 && countDepth1 > 0) || depths.size() == 2;
    }

    public boolean maxDepthHelper(TreeNode node, int depth) {
        if (node != null) {
            depth++;

            if (node.left == null && node.right == null) {
                switch (depths.size()) {
                    case 0 -> depths.add(depth);
                    case 1 -> {
                        if (depths.get(0) != depth) {
                            if (Math.abs(depths.get(0) - depth) == 1) {
                                depths.add(depth);
                            } else {
                                return false;
                            }
                        } else {
                            countDepth1++;
                        }
                    }
                    case 2 -> {
                        return depths.contains(depth);
                    }
                }
                return true;
            }

            boolean depthLeft = maxDepthHelper(node.left, depth);
            boolean depthRight = maxDepthHelper(node.right, depth);

            return depthLeft && depthRight;
        } else {
            return true;
        }
    }
}