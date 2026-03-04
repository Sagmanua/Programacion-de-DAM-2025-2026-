#include <stdio.h>

int main() {
    int dia;
    for(dia = 1; dia <= 31; dia++) {
        // Se agregó el punto y coma (;) que faltaba al final del printf
        printf("Hoy es el dia %i del mes\n", dia);
    }
    
    return 0; 
}