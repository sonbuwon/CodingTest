#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	
	int num, i;
	
	scanf("%d", &num);
	
	int arr[num];
	double arr2[num];
	
	for(i=0;i<num;i++)
	{
		scanf("%d", &arr[i]);
	}
	
	int max = arr[0];
	
	for(i=1;i<num;i++)
	{
		if(max < arr[i])
			max = arr[i];
	}
	
	double total = 0;
	
	for(i=0; i<num; i++)
	{
		arr2[i] = (double) arr[i] / max * 100;
		total += arr2[i];
	}
	
	printf("%lf", total / num);
	
	return 0;
}