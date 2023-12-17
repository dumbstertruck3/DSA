def findMedianSortedArrays(nums1,nums2):
        nums3 = nums1 + nums2
        nums3.sort()
        def is_what(nums):
            if len(nums)%2 == 0:
                return "even"
            else:
                return "odd"
        is_whhat = is_what(nums3)
        if is_whhat == "odd":
            median = len(nums3)//2
            return float(nums3[median])
        else:
             in1 = len(nums3)/2 #index of left center
             in2 = in1 - 1 #index of right center
             median = (nums3[int(in1)] + nums3[int(in2)]) / 2
             return median