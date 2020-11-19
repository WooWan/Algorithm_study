import java.io.IOException;
import java.util.Scanner;

public class BOJ_5639_우창완 {
	//tree 기본 문제
	//class를 새로 정의하는것이 익숙치 않아서 풀이하는데 오래걸렸다
	public static class Node{
		Node left;
		Node right;
		int number;
		Node(int number){
			this.number=number;
		}
	}
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		Node root=new Node(n);
		while(sc.hasNext()) {
			try {
				int number=sc.nextInt();
				insertNode(root, number);
			}catch(Exception e){
				break;
			}
		}
		postorder(root);
	}
	private static void postorder(Node root) {
		if(root.left!=null) postorder(root.left);
		if(root.right!=null) postorder(root.right);
		System.out.println(root.number);
	}
	//자식노드에 따라 recursion을 이용해 풀이한다.
	private static void insertNode(Node root, int number) {
		if(root.number<number) {
			if(root.right==null)	root.right=new Node(number);
			else insertNode(root.right,number);
		}else{
			if(root.left==null)	root.left=new Node(number);
			else insertNode(root.left,number);
		}
	}
}
