import java.util.ArrayList;
import java.util.List;

interface PaymentStrategy {
    public void pay(int amount);
}

class KAKAOCardStrategy implements PaymentStrategy {
    private String email;
    private String pwd;

    public KAKAOCardStrategy(String email, String pwd){
        this.email = email;
        this.pwd = pwd;
    }

    @Override
    public void pay(int amount){
        System.out.println(amount + " paid using KAKAOCard. ");
    }
}

class LUNACardStrategy implements PaymentStrategy {
    private String name;
    private String cardNumber;
    private String cvv;
    private String dateOfExpiry;

    public LUNACardStrategy(String nm, String ccNum, String cvv, String expiryDate){
        this.name = nm;
        this.cardNumber = ccNum;
        this.cvv = cvv;
        this.dateOfExpiry = expiryDate;
    }

    @Override
    public void pay(int amount){
        System.out.println(amount + " paid using LUNACard. ");
    }
}

class Item {
    private String name;
    private int price;
    public Item(String name, int cost){
        this.name = name;
        this.price = cost;
    }

    public String getName() {
        return name;
    }

    public int getPrice() {
        return price;
    }
}

class ShoppingCart {
    List<Item> items;

    public ShoppingCart() {
        this.items = new ArrayList<>();
    }

    public void addItem(Item item){
        this.items.add(item);
    }

    public void removeItem(Item item){
        this.items.remove(item);
    }

    public int calculateTotal() {
        int sum = 0;
        for(Item item : items){
            sum += item.getPrice();
        }
        return sum;
    }

    public void pay(PaymentStrategy paymentMethod){
        int amount = calculateTotal();
        paymentMethod.pay(amount);
    }
}

public class StrategyPattern {
    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();

        Item A = new Item("MacBook", 3000);
        Item B = new Item("IPad", 2000);

        cart.addItem(A);
        cart.addItem(B);

        // 카카오카드로 지불하기
        cart.pay(new KAKAOCardStrategy("tae77777@naver.com", "pukabababo"));

        // 루나카드로 지불하기
        cart.pay(new LUNACardStrategy("Ju hong", "1235", "123","12/01"));
    }
}

/*
*5000 paid using KAKAOCard.
5000 paid using LUNACard.
* */
