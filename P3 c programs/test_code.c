int main() { 
    int a = 5 , 7H; 
    // assign value 
    char b = 'x'; 
    /* return 
    value */ 
    return a + b;  
} 

/* salary calculation*/ 
void main(){ 
    long int bs , da , hra , gs; 
    //take basic salary as input 
    scanf("%ld",&bs); 
    //calculate allowances 
    da=bs*.40; 
    hra=bs*.20; 
    gs=bs+da+hra; 
    // display salary slip 
    printf("\n\nbs  : %ld",bs); 
    printf("\nda  : %ld",da); 
    printf("\nhra : %ld",hra); 
    printf("\ngs  : %ld",gs); 
}  

// user defined data type 
struct student{ 
    int id; 
    float cgpa; 
    } 
    void main( ) 
    { 
    student s; 
    s.id = 10; 
    s.cgpa = 8.7; 
} 

//function prototype 
void add ( int , int ); 
void main( ) 
{ 
    int a , b; 
    a = 10; 
    b = 20; 
    // function call 
    add ( a , b ); 
} 
void add ( int x , int y ) 
{ 
    return x + y; 
} 