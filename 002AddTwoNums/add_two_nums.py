
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
	def add_two_nums(self,lst1,lst2):
		if not lst1:
			return lst2
		if not lst2:
			return lst1
		len1 = len(lst1)
		len2 = len(lst2)
		large_length = max(len1,len2)
		diff = abs(len1-len2)
		if len1>len2:
			lst2 = lst2+[0]*diff
		else:
			lst1 = lst1+[0]*diff
		tmp = 0
		new_list = []
		for i in range(large_length):
			new_list.append((lst1[i]+lst2[i]+tmp)%10)
			tmp = (lst1[i]+lst2[i]+tmp)/10

		tmpn = (new_list[large_length-1]+tmp)/10
		if tmpn ==0:
			return new_list
		else:
			new_list[large_length-1] = (new_list[large_length-1]+tmp)%10
			new_list.append(tmpn)
			return new_list




list1 = [1,2,3,4]
list2 = [2,4,9]
list3 = []

print "\n"
print Solution().add_two_nums(list1,list2)
print "\n"
print Solution().add_two_nums(list2,list3)

