function centuryFromYear(year) {
    var century = 0;
    for(i=0;i<year;i++){
        if(i%100==0){
            century += 1
        }
    }
    return century
}
