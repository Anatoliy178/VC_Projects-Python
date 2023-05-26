int a, b;
Console.Write($"Введите число a: ");
int.TryParse(Console.ReadLine()!, out a);
Console.Write($"Введите число b: ");
int.TryParse(Console.ReadLine()!, out b);

if(a/b == 0) {
  Console.Write("Кратное число");
}
else
{
  Console.WriteLine("Не кратно, остаток: " a%b);
}

// Console.WriteLine(a+b);
