class Factorial{
    public static void main(String[] a){
        System.out.println(new Fac().ComputeFac((10))); 
    }
}
class Fac { // Test
    public int ComputeFac(int num){
        int num_aux ;
        if (num <  2)
            num_aux = 1 ; 
        else
            num_aux = num * (this.ComputeFac(num-1)) ;
        return num_aux ;
    }
}
