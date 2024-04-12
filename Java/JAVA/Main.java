import java.util.concurrent.atomic.AtomicInteger;

public class Main {
    static void increment(AtomicInteger p) {
        p.incrementAndGet();
    }

    public static void main(String[] args) {
        AtomicInteger x = new AtomicInteger(42);
        System.out.println("x = " + x.get()); // prints x = 42
        increment(x);
        System.out.println("x = " + x.get()); // prints x = 43

        int[] arr = {1, 2, 3};
        AtomicInteger q = new AtomicInteger(arr[0]);
        System.out.println("arr[0] = " + q.get()); // prints arr[0] = 1
        q.incrementAndGet();
        System.out.println("arr[1] = " + arr[1]); // prints arr[1] = 2
        q.incrementAndGet();
        System.out.println("arr[2] = " + arr[2]); // prints arr[2] = 3
    }
}
