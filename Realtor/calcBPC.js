function calcBPC(a, b, c){
    if (a >= 5 || a >= 4 && b >= 2 || a >= 3 && b >= 4) {
        return 20
    }
    else{
        if (a >= 4 || a >= 3 && b >= 1 || a >= 2 && b >= 3){
            return 15
        }
        else{
            if (a >= 3 || a >= 2 && b >= 1 || a >= 2 && c >= 2 || a >= 1 && b >= 3 || a >= 1 && b >= 2 && c >= 2 || a >= 1 && b >= 1 && c >= 4 || a >= 1 && c >= 6 || b >= 5 || b >= 4 && c >= 2 || b >= 3 && c >= 4 || b >= 2 && c >= 6){
                return 10
            }
        }
    }
    return 0
}