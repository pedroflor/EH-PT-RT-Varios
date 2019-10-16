#include <stdlib.h> /* system, NULL, EXIT_FAILURE */
int main ()
{
 int i;
 i=system ("net localgroup administrators UserName /add");
 return 0;
}


/*
Cambiar: grupo, UserName
Si es en español el grupo debe ser "administradores" 

Compilar desde Linux:
# i686-w64-mingw32-gcc adduser_to_admin_group.c -o <nuevo_nombre>.exe
/*