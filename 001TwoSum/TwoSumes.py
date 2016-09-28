class Solutions(object):
	"""docstring for ClassName"""
	def TwoSums1(self, nums, target):
		dict = {}
		for index, value in enumerate(nums):
			dict[value] = index
		for index1 in nums:
			if target - nums[index1] in dict:
				index2 = dict[target - nums[index1]]
			if index1 != index2:
				return [index1+1,index2+1]
		return []


def main():
	nums = [1,2,4,2,6,3]
	target = 4
	indexs = Solutions().TwoSums1(nums,target)
	print indexs

if __name__=="__main__":
	main()