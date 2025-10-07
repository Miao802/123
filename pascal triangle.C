#include <stdio.h>

void printPascalTriangle(int rows) {
    for(int i = 0; i < rows; i++) {
        for(int space = 0; space < rows - i - 1; space++) {
            printf("  ");
        }
               
        int number = 1;  
        for(int j = 0; j <= i; j++) {
            printf("%4d", number);
            number = number * (i - j) / (j + 1);
        }
        printf("\n");
    }
}

int main() {
    int rows;
    
    printf("请输入杨辉三角形的行数: ");
    scanf("%d", &rows);
    
    if(rows <= 0) {
        printf("错误：行数必须大于0！\n");
        return 1;
    }
       
    printf("\n%d行杨辉三角形:\n\n", rows);
    printPascalTriangle(rows);
    
    return 0; 
}