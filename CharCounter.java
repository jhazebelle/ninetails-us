import java.util.Scanner;

public class LabProgram {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      String userText;
      int count = 0;
   
      userText = scnr.nextLine();  // Gets entire line, including spaces. 

      // Read through each character in string
      for (int i = 0; i < userText.length(); i++) {
         char currentChar = userText.charAt(i);
         // Check if character is not a space, period, exclamation point or comma
         if (currentChar != ' ' && currentChar != '.' && currentChar != '!' && currentChar != ',') {
            count++;
         }
      }
      
      // Output count
      System.out.println(count);
   }
}
