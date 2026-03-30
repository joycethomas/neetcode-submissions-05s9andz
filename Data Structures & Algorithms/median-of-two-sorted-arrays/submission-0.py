class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(nums2) < len(nums1):
            A, B = nums2, nums1
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 #for A, A[0...i] is the first part
            j = half - i - 2 # for B, B[0...j] is the second part; subtracting 2 because we're trying to get the middle and we need to get rid of the off by one error 
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j>= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright: #if partition is correct
                if total % 2 == 1: # if it's odd
                    return min(Aright, Bright)
                else: #if it's even
                    even = max(Aleft, Bleft) + min(Aright, Bright)
                    return even/2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

            '''if B[j] > A[i + 1]:
                i += 1
                j -= 1
            elif A[i] > B[j + 1]:
                i -= 1
                j += 1
            if A[i] <= B[j + 1] and B[j] <= A[i + 1]:
                if total % 2 == 0:
                    even = max(B[i], A[i]) + min(A[i + 1], B[i + 1])
                    return even/2
                else: 
                    return B[j]'''



        