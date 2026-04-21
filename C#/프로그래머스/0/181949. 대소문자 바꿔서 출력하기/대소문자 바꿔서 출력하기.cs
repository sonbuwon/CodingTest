using System;
public class Example
{
    public static void Main()
    {
        String str = Console.ReadLine();
        String result = "";

        foreach(char c in str) {
            if (char.IsUpper(c)) {
                result += char.ToLower(c);
            }
            else {
                result += char.ToUpper(c);
            }
        }

        Console.WriteLine(result);
    }
}