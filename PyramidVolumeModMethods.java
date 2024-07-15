import java.util.Scanner;

public class CalcPyramidVolume {

   public static double calcBaseArea(double baseLength, double baseWidth) {
      return baseLength * baseWidth;
   }

   public static double calcPyramidVolume(double baseLength, double baseWidth, double pyramidHeight) {
      double baseArea = calcBaseArea(baseLength, baseWidth);
      return baseArea * pyramidHeight / 3.0;
   }

   public static void main (String [] args) {
      Scanner scnr = new Scanner(System.in);
      double userLength;
      double userWidth;
      double userHeight;

      userLength = scnr.nextDouble();
      userWidth = scnr.nextDouble();
      userHeight = scnr.nextDouble();

      System.out.println("Volume: " + calcPyramidVolume(userLength, userWidth, userHeight));
   }
}
