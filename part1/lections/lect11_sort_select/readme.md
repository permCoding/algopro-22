Лекция 11  

## задания к лабраб по этой Лекции  

___Код оформляйте в виде функций...___  

#### task_01  

- исправить функцию sort_select()  
- должна работать правильно, но тут есть неточность:  

```py
def sort_select(arr):
    for n in range(len(arr), 0, -1):
        ind_max = 0
        for i in range(n):
            if arr[i] > arr[ind_max]:
                ind_max = i
        arr[ind_max], arr[-1] = arr[n-1], arr[ind_max]
    return arr
```

---  

#### task_02  

- сортировать целые числа по количеству делителей  
- использовать встроенную в Питон функцию sorted()  
- и в ней настроить ключ сортировки  
- для ключа сортировки создать функцию get_count_div, которая будет возвращать количество делителей  

---  

#### task_03  

- данные по абитуриентам приведены в файле abiturs.txt (скопировать данные ниже и поместить в файл вручную перед наприсанием программы)  

```txt
id,name,age,rait
1,Алекс,18,197
2,Митя,19,182
3,Саша,18,197
4,Саня,19,234
5,Коленька,18,201
6,Гоген,18,200
7,Стас,19,235
```

- считать данные из файла и отсортировать (используя функцию Питона sorted()) по рейтингу в убывающем порядке  
- сохранить в файл best.txt троих лучших по рейтингу, например:  
```txt
id,name,age,rait
7,Стас,19,235
4,Саня,19,234
6,Гоген,18,201
```

---  
