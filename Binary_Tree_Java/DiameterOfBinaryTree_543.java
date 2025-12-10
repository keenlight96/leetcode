
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;



public class DiameterOfBinaryTree_543 {
    private int maxDiameter = 0;
    public static void main(String[] args) {
        Integer[] arr1 = {4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2};
        List<Integer> arr = new ArrayList<>(Arrays.asList(arr1));
        TreeNode root = HelperBinaryTree.arrayToBinaryTree(arr);
        
        DiameterOfBinaryTree_543 solution = new DiameterOfBinaryTree_543();
        int diameter = solution.diameterOfBinaryTree(root);

        System.err.println(diameter);
    }

    public int diameterOfBinaryTree(TreeNode root) {
        maxDepthHelper(root, 0);
        return maxDiameter;
    }

    public int maxDepthHelper(TreeNode node, int depth) {
        if (node != null) {
            depth++;
            int left = maxDepthHelper(node.left, depth);
            int right = maxDepthHelper(node.right, depth);
            
            int currentDiameter = (left - depth) + (right - depth);
            if (currentDiameter > maxDiameter) {
                maxDiameter = currentDiameter;
            }
            return left > right ? left : right;
        } else {
            return depth;
        }
    }
}