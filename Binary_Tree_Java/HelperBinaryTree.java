import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class HelperBinaryTree {
    public static void main(String[] args) {
        
    }

    public static ArrayList<Integer> convertTreeNodeToArray(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList = convertTreeNodeToArrayHelper(arrayList, root, 0);
        return arrayList;
    }

    public static ArrayList<Integer> convertTreeNodeToArrayHelper(ArrayList<Integer> arrayList, TreeNode node, int index) {
        while (index >= arrayList.size()) {
            arrayList.add(null);
        }
        arrayList.set(index, node.val);
        if (node.left != null) {
            arrayList = convertTreeNodeToArrayHelper(arrayList, node.left, index * 2 + 1);
        }
        if (node.right != null) {
            arrayList = convertTreeNodeToArrayHelper(arrayList, node.right, index * 2 + 2);
        }
        return arrayList;
    }

    public static TreeNode convertArrayToTreeNode(Integer[] arr) {
        TreeNode root = convertArrayToTreeNodeHelper(arr, 0);
        return root;
    }

    public static TreeNode arrayToBinaryTree(List<Integer> arr) {
        if (arr.isEmpty()) {
            return null;
        }

        Queue<TreeNode> nodes = new LinkedList<>();
        int val = arr.remove(0);
        TreeNode root = new TreeNode(val);
        nodes.add(root);

        while (!arr.isEmpty()) {
            TreeNode curr = nodes.poll();

            if (!arr.isEmpty()) {
                Integer leftVal = arr.remove(0);
                if (leftVal != null) {
                    curr.left = new TreeNode(leftVal);
                    nodes.add(curr.left);
                }
            }

            if (!arr.isEmpty()) {
                Integer rightVal = arr.remove(0);
                if (rightVal != null) {
                    curr.right = new TreeNode(rightVal);
                    nodes.add(curr.right);
                }
            }
        }

        return root;
    }

    public static TreeNode convertArrayToTreeNodeHelper(Integer[] arr, int index) {
        if (index >= arr.length || arr[index] == null) {
            return null;
        }
        TreeNode node = new TreeNode(arr[index]);
        node.left = convertArrayToTreeNodeHelper(arr, index * 2 + 1);
        node.right = convertArrayToTreeNodeHelper(arr, index * 2 + 2);
        return node;
    }
}
