#include <stdio.h>

int main(void)
{
  int contador = 1; //variável de controle do loop
  int soma = 0;
  while(contador <= 100)
  {
      soma = soma + contador;
      contador ++;
  }
  printf("A soma de 1 até 100 é: %d\n", soma);
  return(0);
}
