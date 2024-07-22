import java.util.Scanner;

public class ForLoops {
   public static void main (String [] args) {
      int userNum;
      int i;
      
      Scanner input = new Scanner(System.in);
      userNum = input.nextInt();

      System.out.println("Ready!");
      for (i = userNum; i >= 1; i--) {
         System.out.println(i);
      }

      // Print "Blastoff!" followed by a newline
      System.out.println("Blastoff!");

   }
}
