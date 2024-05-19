public class Fibonacci {
    private static int k,g;
    private static int fib(int n) {
        if ((n == 2) || (n == 1)) {
            return 1;
        }
        else {
            k = fib(n-1) + fib(n-2);
            return k;
        }
    }
    public static int fib2(int n) {
        if (n < 1) {
            throw new IllegalArgumentException("n cannot be less than 0.");
        }
        else {
            g = fib(n);
            System.out.println(g);
            return g;
        }
    }
}
