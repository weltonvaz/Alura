#include <stdio.h>

int main()
{
    int num1, num2, resultado;
    printf("Digite um numero: ");
    scanf("%d", &num1);

    printf("Digite outro numero: ");
    scanf("%d", &num2);
    printf("\n");
    resultado = num1 + num2;

    printf("%d * %d = %d\n", num1,num2,resultado);
}