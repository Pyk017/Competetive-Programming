int maxPathSum(int ar1[], int ar2[])
    {
        int sum1 = 0, sum2 =0,totalSum=0;
        List<int[]> list = new ArrayList<>();
        int i=0,j=0;
        while(i<ar1.length&&j<ar2.length){
            if(ar1[i]==ar2[j]){
                list.add(new int[]{i,j});
                i++;
                j++;
            }else if(ar1[i]>ar2[j]){
                j++;
            }else{
                i++;
            }
        }
        i=0;
        j=0;
        list.add(new int[]{ar1.length-1,ar2.length-1});
        for(int[] x: list){
            for(;i<=x[0];i++){
                sum1+=ar1[i];
            }
            for(;j<=x[1];j++){
                sum2+=ar2[j];
            }
            totalSum+=Math.max(sum1,sum2);
            sum1=sum2=0;
        }
        return totalSum;
    }