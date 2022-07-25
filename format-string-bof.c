#include<stdio.h>
#include<string.h>
char dum[5]="abc";
char change[5]="dummy";
int main()
{
	char temp[1337];
	fgets(temp,6,stdin);
	sprintf(dum,temp);
	printf("Size is %d\n",strlen(dum));
	printf(change);
	if (strcmp(change,"dummy")!=0){
printf("You won maara!");
	}
	else{
		printf("Try harder!!");
	}
	
}


#exploit is %100c
