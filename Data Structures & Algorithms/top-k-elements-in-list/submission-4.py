class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numbers = sorted(nums)

        k_elements = defaultdict(int)

        result = []

        i=0

        for s in numbers:
            if s in k_elements:
                k_elements[s] += 1
            else:
                k_elements[s] = 1

        print(k_elements)

        while i < k:
            for keys,values in list(k_elements.items()):
                result.append(max(k_elements , key = k_elements.get))
                del k_elements[max(k_elements , key = k_elements.get)]
                print(k_elements)
                i = i+1
                if i == k:
                    break

        return result


        