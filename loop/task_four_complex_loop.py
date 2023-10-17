def pascal(n):
  """
  Mencetak pola segitiga Pascal

  Args:
    n: Jumlah baris pada segitiga

  Returns:
    None
  """
  for i in range(n + 1):
    print(" " * (n - i), end="")
    for j in range(i + 1):
      print(f"{pascal_coef(i, j)}", end=" ")
    print()

def pascal_coef(n, k):
  """
  Menghitung koefisien binomial

  Args:
    n: Jumlah elemen dalam kumpulan
    k: Jumlah elemen yang dipilih

  Returns:
    Koefisien binomial
  """
  if k > n:
    return 0
  elif k == 0 or k == n:
    return 1
  else:
    return pascal_coef(n - 1, k - 1) + pascal_coef(n - 1, k)

def prime_number():
  for i in range(2, 101):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      print(i)

def is_palindrome(n):
  """
  Memeriksa apakah suatu angka adalah palindrom

  Args:
    n: Angka yang akan diperiksa

  Returns:
    True jika angka tersebut adalah palindrom, False jika tidak
  """
  str_n = str(n)
  return str_n == str_n[::-1]

def print_palindromes(n):
  """
  Mencetak angka palindrom dari 1 hingga n

  Args:
    n: Angka terakhir yang akan dicetak

  Returns:
    None
  """
  i = 1
  while i <= n:
    if is_palindrome(i):
      print(i)
    i += 1

if __name__ == '__main__':
  print_palindromes(100)