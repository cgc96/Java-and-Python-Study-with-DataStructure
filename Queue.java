import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

class Queue {
	
	private Node head;
	private Node tail;
	private int QueueSize;
	
	private class Node{
		private Object data;
		private Node nextNode;
		
		Node(Object data){
			this.data = data;
			this.nextNode = null;
		}
	}
	
	public Queue() { //Queue의 기본 생성자 세
		this.head = null;
		this.tail = null;
		this.QueueSize = 0;
	}
	
	int isEmpty() {
		if(this.head == null) // head가 null이면 Queue가 Empty
			return 1;
		return 0;
		
	}
	
	void Enqueue(Object item) {
		Node newNode = new Node(item); // 새 노드 생
		
		if(this.head == null) { // 큐에 아무 node가 없는 경우 
			this.head = newNode; // head랑 tail에 새 node저장 
			this.tail = newNode;
		}else { // 큐에 node가 있는 경우 
			this.tail.nextNode = newNode; // tail의 next에 새 node 저장  
			this.tail = this.tail.nextNode; // tail을 새 node로 업데이트 
		}
		this.QueueSize += 1; //Queue size 1증가 
	}
	
	Object Dequeue() {
		if(this.isEmpty() == 1) // Queue가 비어있으면 return -1
			return -1;
		
		Object ret_data = this.head.data; //head의 data return
		this.head = this.head.nextNode; // head를 다음 node로 업데이트 
		
		if(this.head == null) //head가 null을 가리키면 tail도 null로 업데이트 
			this.tail = null;
		
		this.QueueSize -= 1; //Queue size1감소 
		return ret_data;
	}
	
	Object front() { //head의 data return 
		if(isEmpty() == 1)
			return -1;
		else
			return this.head.data;
	}
	
	Object back() { //tail의 data return 
		if(isEmpty() == 1)
			return -1;
		else
			return this.tail.data;
	}
	
	int Size() { //Queue의 size return 
		return this.QueueSize;
	}
	
	public static int n;
	
	public static void main(String[] args) throws IOException{
		
		Scanner scan = new Scanner(System.in);
		n = Integer.parseInt(scan.next());
		
		Queue Q = new Queue();
		
		for(int i = 0; i < n; i++) {
			String s = scan.next();
			if(s.equals("back")) {
				System.out.println(Q.back());
			}else if(s.equals("pop")) {
				System.out.println(Q.Dequeue());
			}else if(s.equals("size")) {
				System.out.println(Q.Size());
			}else if(s.equals("empty")) {
				System.out.println(Q.isEmpty());
			}else if(s.equals("front")) {
				System.out.println(Q.front());
			}else {
				int k = Integer.parseInt(scan.next());
				Q.Enqueue(k);
			}
		}
	}
}

