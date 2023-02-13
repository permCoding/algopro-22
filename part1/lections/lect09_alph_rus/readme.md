## задания к лабраб по этой Лекции  

___Код, по возможности, оформляйте в виде функций...___  

#### task_01  

- пользователь вводит НГ и ВГ  
- программа в ответ выводит таблицу символов в два столбика - номер символа в таблице символов и сам вид символа  
- например, для НГ=49 и ВГ=53 корректный ответ такой:  
```txt
49 1
50 2
51 3
52 4
53 5
```

---  

#### task_02  

- пользователь вводит НГ и ВГ  
- программа в ответ выводит таблицу символов в виде квадрата или фигуры максимально близкой к квадрату  
- например, для НГ = 33 и ВГ=51 будет построена такая таблица:  
```txt
! " # $
% & ' (
) * + ,
- . / 0
1 2 3
```

---  

#### task_03  

- пусть НГ=32 и ВГ=127 назначены программой  
- это сделано для того, чтобы итоговая таблица смотрелась аккуратно, а номер строки и номер столбца обозначались одной шестнадцатиричной цифрой  
- программа в ответ выводит таблицу символов в виде прямоугольника, где символ можно найти на пересечении номера строки и номера столбца, которые кодируются шестнадцатеричной цифрой  
- дополнительно вдоль верхней и вдоль левой границы таблицы для удобства пользователя следует разместить шестнадцатеричные значения позиции символа, например у позиции 74 (это в 10-ой СС) шестнадцатеричный эквивалент = 4A, поэтому номер строки 4 и номер столбца A  
- пример такой таблицы:  
```txt
  0 1 2 3 4 5 6 7 8 9 A B C D E F 
2   ! " # $ % & ' ( ) * + , - . / 
3 0 1 2 3 4 5 6 7 8 9 : ; < = > ? 
4 @ A B C D E F G H I J K L M N O
5 P Q R S T U V W X Y Z [ \ ] ^ _ 
6 ` a b c d e f g h i j k l m n o 
7 p q r s t u v w x y z { | } ~ ⌂ 
```
Пользователь может взять из строки 3 и столбца 0 символ '0'. Позицию символа пользователь может сам привести и к десятичному виду, например, если позиция в шестнадцатеричной СС = 30, то в десятичной это будет 3*16 + 0 = 48. И действительно на позиции 48 в таблице символов находится символ '1'.  

---  