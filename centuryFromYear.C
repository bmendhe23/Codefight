int centuryFromYear(int year) {
    int century=0;
    for(int i=0;i<year;i++){
        if(i%100==0){
            century+=1;
        }
    }
    return(century);
}
