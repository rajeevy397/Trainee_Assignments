package NumberCheck;

public class NumberCheck {
    public static void main(String[] args) {
        checkNumber(5); // 5 is positive
        checkNumber(-3); // -3 is negative
        checkNumber(0); // 0 is zero
    }

    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println(num + " is positive");
        } else if (num < 0) {
            System.out.println(num + " is negative");
        } else {
            System.out.println(num + " is zero");
        }
    }
}
