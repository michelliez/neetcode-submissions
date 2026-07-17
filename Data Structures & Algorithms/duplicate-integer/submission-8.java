class Solution {
    public boolean hasDuplicate(int[] nums) {
        java.util.HashSet<Integer> myHash = new java.util.HashSet<>();
        for (int num: nums){
            if (myHash.contains(num)){
                return true;
            }
            myHash.add(num);
        }
        return false;
    }
}