import java.io.*;
import java.util.*;

public class java {
    public static void main(String[] args) throws IOException {
        Scanner inputScanner = new Scanner(System.in);
        System.out.print("Dateiname: ");
        String filename = inputScanner.nextLine();

        BufferedReader reader = new BufferedReader(new FileReader(filename));
        int figures = Integer.parseInt(reader.readLine());
        int books = Integer.parseInt(reader.readLine());
        List<Integer> shelf = new ArrayList<>();

        for (int i = 0; i < books; i++) {
            shelf.add(Integer.parseInt(reader.readLine()));
        }

        Collections.sort(shelf);
        int curmin = shelf.get(0);

        for (int book : shelf) {
            if (book - curmin > 30) {
                curmin = book;
                figures--;
            }
        }

        if (figures < 0) {
            System.out.println("Geht nicht");
        } else {
            System.out.println("Geht");
        }

        reader.close();
    }
}