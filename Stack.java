import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Stack {
	
	private Node top;
	
	private class Node{
		private Object data;
		private Node nextNode;
		Node(Object data){
			this.data = data;
			this.nextNode = null;
		}
	}
	
	public Stack() {
		this.top = null;
	}
	
	void push(Object item) {
		Node newNode = new Node(item);
		newNode.nextNode = top;
		top = newNode;
	}
	
	public Object pop() {
		Object item = peek();
		top = top.nextNode;
		return item;
	}
	
	public boolean empty() {
		return (top == null);
	}
	
	public Object peek() {
		if(empty())
			throw new ArrayIndexOutOfBoundsException();
		return top.data;
	}
	
	public static int n;
	public static int num = 1;
	public static int[] arr;
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		arr = new int[n];
		Stack st = new Stack();
		
		boolean isAble = true;
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		
			if(isAble) {
				if(num <= arr[i]) {
					while(num <= arr[i]) {
						st.push(num++);
						sb.append("+ \n");
					}
				}
				if(st.empty())
					isAble = false;
				else {
					while((Integer)st.peek() >= arr[i]) {
						st.pop();
						sb.append("- \n");
						if(st.empty())
							break;
					}
				}
			}
		}
		if(isAble)
			System.out.println(sb.toString());
		else
			System.out.println("NO");
	}
}
