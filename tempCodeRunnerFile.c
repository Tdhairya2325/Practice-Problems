for(int i=0;i<n/2;i++){
  for(int j=0;j<n-i-1;j++){
    printf(" ");
  }
  for(int k=0;k<2*i+1;k++){
    printf("*");
  }
  printf("\n");
}