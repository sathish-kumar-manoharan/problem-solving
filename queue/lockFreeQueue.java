import java.util.concurrent.atomic.AtomicReference;

public class ConcurrentQueue<T> {
    private static class Node<T> {
        T data;
        AtomicReference<Node<T>> next;

        Node(T value) {
            data = value;
            next = new AtomicReference<>(null);
        }
    }

    private final AtomicReference<Node<T>> head;
    private final AtomicReference<Node<T>> tail;

    public ConcurrentQueue() {
        Node<T> sentinel = new Node<>(null);
        head = new AtomicReference<>(sentinel);
        tail = new AtomicReference<>(sentinel);
    }

    public void enqueue(T value) {
        Node<T> newNode = new Node<>(value);
        while (true) {
            Node<T> curTail = tail.get();
            Node<T> curNext = curTail.next.get();
            if (curTail == tail.get()) {
                if (curNext == null) {
                    if (curTail.next.compareAndSet(null, newNode)) {
                        tail.compareAndSet(curTail, newNode);
                        return;
                    }
                } else {
                    tail.compareAndSet(curTail, curNext);
                }
            }
        }
    }

    public boolean dequeue(T[] result) {
        while (true) {
            Node<T> curHead = head.get();
            Node<T> curTail = tail.get();
            Node<T> curNext = curHead.next.get();
            if (curHead == head.get()) {
                if (curHead == curTail) {
                    if (curNext == null) {
                        return false;
                    }
                    tail.compareAndSet(curTail, curNext);
                } else {
                    result[0] = curNext.data;
                    if (head.compareAndSet(curHead, curNext)) {
                        return true;
                    }
                }
            }
        }
    }
}